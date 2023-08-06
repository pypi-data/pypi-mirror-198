from datetime import datetime
from typing import List
from typing import Mapping
from typing import Optional
from typing import Union

import pandas as pd
import pendulum
import pyspark
from pyspark.sql import functions

from tecton import conf
from tecton._internals import data_frame_helper
from tecton._internals import errors as internal_errors
from tecton._internals.feature_views import aggregations
from tecton._internals.utils import is_bfc_mode_single
from tecton._internals.utils import is_live_workspace
from tecton.interactive.data_frame import DataFrame
from tecton.tecton_context import TectonContext
from tecton.tecton_errors import TectonValidationError
from tecton_proto.args.pipeline_pb2 import PipelineNode
from tecton_spark.fco_container import FcoContainer
from tecton_spark.feature_definition_wrapper import FeatureDefinitionWrapper as FeatureDefinition
from tecton_spark.feature_set_config import FeatureDefinitionAndJoinConfig
from tecton_spark.id_helper import IdHelper
from tecton_spark.logger import get_logger
from tecton_spark.materialization_params import MaterializationParams
from tecton_spark.query_utils import add_effective_timestamp
from tecton_spark.query_utils import EFFECTIVE_TIMESTAMP
from tecton_spark.schema_spark_utils import schema_to_spark

logger = get_logger("FeatureRetrieval")


def get_features(
    fd: FeatureDefinition,
    entities: Optional[Union[pyspark.sql.dataframe.DataFrame, pd.DataFrame, DataFrame]] = None,
    start_time: Optional[Union[pendulum.DateTime, datetime]] = None,
    end_time: Optional[Union[pendulum.DateTime, datetime]] = None,
    from_source: bool = False,
) -> DataFrame:
    if fd.is_on_demand:
        raise internal_errors.FV_NOT_SUPPORTED_GET_HISTORICAL_FEATURES

    if from_source and fd.is_feature_table:
        raise TectonValidationError("FeatureTables are not compatible with from_source=True")

    if from_source and is_bfc_mode_single(fd):
        raise internal_errors.FV_BFC_SINGLE_FROM_SOURCE

    if not from_source and not is_live_workspace(fd.workspace):
        raise internal_errors.FD_GET_MATERIALIZED_FEATURES_FROM_DEVELOPMENT_WORKSPACE(fd.name, fd.workspace)

    if not from_source and not fd.writes_to_offline_store:
        raise internal_errors.FD_GET_FEATURES_MATERIALIZATION_DISABLED(fd.name)

    if start_time is not None and isinstance(start_time, datetime):
        start_time = pendulum.instance(start_time)
    if end_time is not None and isinstance(end_time, datetime):
        end_time = pendulum.instance(end_time)

    if start_time is not None and fd.feature_start_timestamp is not None and start_time < fd.feature_start_timestamp:
        logger.warning(
            f'The provided start_time ({start_time}) is before "{fd.name}"\'s feature_start_time ({fd.feature_start_timestamp}). No feature values will be returned before the feature_start_time.'
        )
        start_time = fd.feature_start_timestamp

    if fd.is_temporal_aggregate or fd.is_temporal:
        params = MaterializationParams.from_feature_definition(fd)
        assert params is not None, "Materialization params cannot be None"
        # Feature views where materialization is not enabled may not have a feature_start_time.
        _start = start_time or fd.feature_start_timestamp or pendulum.datetime(1970, 1, 1)
        # we need to add 1 to most_recent_anchor since we filter end_time exclusively
        _end = end_time or (params.most_recent_anchor(pendulum.now("UTC")) + pendulum.duration(microseconds=1))
    else:
        _start = start_time or pendulum.datetime(1970, 1, 1)
        _end = end_time or pendulum.now("UTC")

    time_range = pendulum.Period(_start, _end)

    tc = TectonContext.get_instance()
    spark = tc._spark

    # Validate that entities only contains Join Key Columns.
    if entities is not None:
        if isinstance(entities, pd.DataFrame):
            entities = spark.createDataFrame(entities)
        if isinstance(entities, DataFrame):
            entities = entities.to_spark()
        assert set(entities.columns).issubset(
            set(fd.join_keys)
        ), f"Entities should only contain columns that can be used as Join Keys: {fd.join_keys}"

    try:
        batch_schedule_seconds = int(fd.fv.materialization_params.schedule_interval.ToTimedelta().total_seconds())
        data_delay_seconds = fd.online_store_data_delay_seconds
        if fd.is_temporal or fd.is_feature_table:
            df = aggregations.get_all_temporal_ft_features(spark, fd, entities, not from_source, time_range)
            if conf.get_bool("DATA_SKEW_REDUCTION"):
                df = add_effective_timestamp(
                    df,
                    effective_timestamp_name=EFFECTIVE_TIMESTAMP,
                    batch_schedule_seconds=batch_schedule_seconds,
                    data_delay_seconds=data_delay_seconds,
                    timestamp_field=fd.timestamp_key,
                    is_stream=fd.is_stream,
                    is_temporal_aggregate=False,
                )
        else:
            df = data_frame_helper._get_feature_dataframe_with_limits(
                fd,
                spine=None,
                spine_time_limits=time_range,
                use_materialized_data=not from_source,
                spine_time_key=None,
                validate_time_key=False,
            ).to_spark()
            if entities is not None:
                df = df.join(functions.broadcast(entities.distinct()), entities.columns, how="right")
            columns = fd.join_keys + fd.features + [fd.timestamp_key]
            if conf.get_bool("DATA_SKEW_REDUCTION"):
                df = add_effective_timestamp(
                    df,
                    effective_timestamp_name=EFFECTIVE_TIMESTAMP,
                    batch_schedule_seconds=batch_schedule_seconds,
                    data_delay_seconds=data_delay_seconds,
                    timestamp_field=fd.timestamp_key,
                    is_stream=fd.is_stream,
                    is_temporal_aggregate=True,
                )
                columns.append(EFFECTIVE_TIMESTAMP)
            df = df.select(*columns)
    except pyspark.sql.utils.AnalysisException as e:
        if "Unable to infer schema for Parquet" in e.desc or "doesn't exist" in e.desc:
            if fd.is_feature_table:
                return DataFrame._create(tc._spark.createDataFrame([], schema_to_spark(fd.view_schema)))
            else:
                raise internal_errors.FV_NO_MATERIALIZED_DATA(fd.name)
        raise

    # Temporal feature views derived directly from raw data should already filtered to this timerange, but all other
    # cases may have data outside of this range. Apply this filter in all cases to be safe.
    if _start:
        df = df.filter(df[fd.timestamp_key] >= _start)
    if _end:
        df = df.filter(df[fd.timestamp_key] < _end)

    return DataFrame._create(df)


def find_dependent_feature_set_items(
    fco_container: FcoContainer, node: PipelineNode, visited_inputs: Mapping[str, bool], fv_id: str, workspace_name: str
) -> List[FeatureDefinitionAndJoinConfig]:
    if node.HasField("feature_view_node"):
        if node.feature_view_node.input_name in visited_inputs:
            return []
        visited_inputs[node.feature_view_node.input_name] = True

        fv_proto = fco_container.get_by_id(IdHelper.to_string(node.feature_view_node.feature_view_id))
        fd = FeatureDefinition(fv_proto, fco_container)

        join_keys = []
        overrides = {
            colpair.feature_column: colpair.spine_column
            for colpair in node.feature_view_node.feature_view.override_join_keys
        }
        for join_key in fv_proto.join_keys:
            potentially_overriden_key = overrides.get(join_key, join_key)
            join_keys.append((potentially_overriden_key, join_key))

        cfg = FeatureDefinitionAndJoinConfig(
            feature_definition=fd,
            name=fd.name,
            join_keys=join_keys,
            namespace=f"_udf_internal_{node.feature_view_node.input_name}_{fv_id}",
            features=node.feature_view_node.feature_view.features or fd.features,
        )

        return [cfg]
    elif node.HasField("transformation_node"):
        ret: List[FeatureDefinitionAndJoinConfig] = []
        for child in node.transformation_node.inputs:
            ret = ret + find_dependent_feature_set_items(
                fco_container, child.node, visited_inputs, fv_id, workspace_name
            )
        return ret
    return []
