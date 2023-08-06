import tempfile
from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import pandas as pd
import pendulum
from pyspark.sql import DataFrame
from pyspark.sql.streaming import StreamingQuery

from tecton import conf
from tecton._internals import errors
from tecton._internals import metadata_service
from tecton._internals.display import Displayable
from tecton._internals.sdk_decorators import sdk_public_method
from tecton.fco import Fco
from tecton.interactive import snowflake_api
from tecton.interactive.data_frame import DataFrame as TectonDataFrame
from tecton.tecton_context import TectonContext
from tecton_proto.common.id_pb2 import Id
from tecton_proto.data.batch_data_source_pb2 import BatchDataSource as BatchDataSourceProto
from tecton_proto.data.stream_data_source_pb2 import StreamDataSource as StreamDataSourceProto
from tecton_proto.data.virtual_data_source_pb2 import VirtualDataSource as VirtualDataSourceProto
from tecton_proto.metadataservice.metadata_service_pb2 import GetVirtualDataSourceRequest
from tecton_proto.metadataservice.metadata_service_pb2 import GetVirtualDataSourceSummaryRequest
from tecton_spark import data_source_helper
from tecton_spark.fco_container import FcoContainer
from tecton_spark.feature_definition_wrapper import FrameworkVersion
from tecton_spark.id_helper import IdHelper
from tecton_spark.logger import get_logger

logger = get_logger("DataSource")


class BaseDataSource(Fco):
    ds_proto: VirtualDataSourceProto
    batch_ds: BatchDataSourceProto
    stream_ds: Optional[StreamDataSourceProto]
    fco_container: FcoContainer

    @classmethod
    def _from_proto_and_data_sources(
        cls,
        ds_proto: VirtualDataSourceProto,
        fco_container: FcoContainer,
        batch_ds: Optional[BatchDataSourceProto],
        stream_ds: Optional[StreamDataSourceProto],
    ) -> "BaseDataSource":
        """
        Create a new data source instance.
        :param ds_proto: VirtualDataSource proto to be unpacked into a class instance.
        :param batch_ds: BatchDataSource instance representing batch DS to be included
                         into this DS.
        :param stream_ds: Optional StreamDataSource instance representing streaming DS to be
                          included into this DS. If present, this DS class
                          represents a stream DS backed up with a batch DS.
        """
        obj = cls.__new__(cls)
        obj.ds_proto = ds_proto
        obj.fco_container = fco_container
        obj.batch_ds = batch_ds
        obj.stream_ds = stream_ds
        return obj

    @classmethod
    def _create_from_proto(cls, ds_proto, fco_container: FcoContainer) -> "BaseDataSource":
        """
        Creates a new :class:`BaseDataSource` class from persisted Virtual DS proto.

        :param ds_proto: VirtualDataSource proto struct.
        :param fco_container: FcoContainer object.
        :return: :class:`BaseDataSource` class instance.
        """
        batch_ds = ds_proto.batch_data_source
        stream_ds = None
        if ds_proto.HasField("stream_data_source"):
            stream_ds = ds_proto.stream_data_source

        return cls._from_proto_and_data_sources(ds_proto, fco_container, batch_ds, stream_ds)

    @property  # type: ignore
    @sdk_public_method
    def is_streaming(self) -> bool:
        """
        Whether or not it's a StreamDataSource.
        """
        return self.stream_ds is not None

    @property  # type: ignore
    @sdk_public_method
    def columns(self) -> List[str]:
        """
        Returns streaming DS columns if it's present. Otherwise, returns batch DS columns.
        """
        if self.is_streaming:
            assert self.stream_ds is not None
            schema = self.stream_ds.spark_schema
        else:
            schema = self.ds_proto.batch_data_source.spark_schema

        return [field.name for field in schema.fields]

    @property
    def _proto(self):
        """
        Returns VirtualDataSource proto.
        """
        return self.ds_proto

    @classmethod
    def _fco_type_name_singular_snake_case(cls) -> str:
        return "data_source"

    @classmethod
    def _fco_type_name_plural_snake_case(cls) -> str:
        return "data_sources"

    @property
    def _fco_metadata(self):
        return self._proto.fco_metadata

    def _id_proto(self) -> Id:
        return self._proto.virtual_data_source_id

    @property  # type: ignore
    @sdk_public_method
    def id(self) -> str:
        """
        Returns a unique ID for the data source.
        """
        return IdHelper.to_string(self._id_proto())

    def _get_stream_preview_dataframe(
        self, apply_translator, option_overrides: Optional[Dict[str, str]] = None
    ) -> DataFrame:
        """
        Helper function that allows start_stream_preview(apply_translator)
        to be unit tested, since we can't easily unit test writing to temporary tables.
        """
        if not self.is_streaming:
            raise errors.DS_STREAM_PREVIEW_ON_NON_STREAM
        spark = TectonContext.get_instance()._spark
        if apply_translator:
            return data_source_helper.get_stream_dataframe_with_options(spark, self.stream_ds, option_overrides)
        else:
            return data_source_helper.get_raw_stream_dataframe(spark, self.stream_ds, option_overrides)

    @sdk_public_method
    def start_stream_preview(
        self, table_name: str, *, apply_translator: bool = True, option_overrides: Optional[Dict[str, str]] = None
    ) -> StreamingQuery:
        """
        Starts a streaming job to write incoming records from this DS's stream to a temporary table with a given name.

        After records have been written to the table, they can be queried using ``spark.sql()``. If ran in a Databricks
        notebook, Databricks will also automatically visualize the number of incoming records.

        This is a testing method, most commonly used to verify a StreamDataSource is correctly receiving streaming events.
        Note that the table will grow infinitely large, so this is only really useful for debugging in notebooks.

        :param table_name: The name of the temporary table that this method will write to.
        :param apply_translator: Whether to apply this data source's ``raw_stream_translator``.
            When True, the translated data will be written to the table. When False, the
            raw, untranslated data will be written.
        :param option_overrides: A dictionary of Spark readStream options that will override any readStream options set
            by the data source. Can be used to configure behavior only for the preview, e.g. setting
            ``startingOffsets:latest`` to preview only the most recent events in a Kafka stream.
        """
        df = self._get_stream_preview_dataframe(apply_translator, option_overrides)

        with tempfile.TemporaryDirectory() as d:
            return (
                df.writeStream.format("memory")
                .queryName(table_name)
                .option("checkpointLocation", d)
                .outputMode("append")
                .start()
            )

    @sdk_public_method
    def get_dataframe(
        self,
        start_time: Optional[Union[pendulum.DateTime, datetime]] = None,
        end_time: Optional[Union[pendulum.DateTime, datetime]] = None,
        *,
        apply_translator: bool = True,
    ) -> TectonDataFrame:
        """
        Returns this data source's data as a Tecton DataFrame.

        :param start_time: The interval start time from when we want to retrieve source data.
            If no timezone is specified, will default to using UTC.
            Can only be defined if ``apply_translator`` is True.
        :param end_time: The interval end time until when we want to retrieve source data.
            If no timezone is specified, will default to using UTC.
            Can only be defined if ``apply_translator`` is True.
        :param apply_translator: If True, the transformation specified by ``raw_batch_translator``
            will be applied to the dataframe for the data source.

        :return: A Tecton DataFrame containing the data source's raw or translated source data.

        :raises TectonValidationError: If ``apply_translator`` is False, but ``start_time`` or
            ``end_time`` filters are passed in.
        """
        if conf.get_bool("ALPHA_SNOWFLAKE_COMPUTE_ENABLED"):
            return snowflake_api.get_dataframe_for_data_source(self.batch_ds, start_time, end_time)

        spark = TectonContext.get_instance()._spark

        if apply_translator:
            if self.is_streaming:
                timestamp_key = self.stream_ds.time_column
            else:
                timestamp_key = self.batch_ds.timestamp_column_properties.column_name
            if not timestamp_key and (start_time or end_time):
                raise errors.DS_DATAFRAME_NO_TIMESTAMP

            df = data_source_helper.get_ds_dataframe(
                spark,
                data_source=self.ds_proto,
                consume_streaming_data_source=False,
                start_time=start_time,
                end_time=end_time,
            )
        else:
            if start_time is not None or end_time is not None:
                raise errors.DS_RAW_DATAFRAME_NO_TIMESTAMP_FILTER

            df = data_source_helper.get_raw_dataframe(spark, self.batch_ds)

        return TectonDataFrame._create(df)

    @sdk_public_method
    def summary(self) -> Displayable:
        """
        Displays a human readable summary of this data source.
        """
        request = GetVirtualDataSourceSummaryRequest()
        request.fco_locator.id.CopyFrom(self.ds_proto.virtual_data_source_id)
        request.fco_locator.workspace = self.workspace

        response = metadata_service.instance().GetVirtualDataSourceSummary(request)
        return Displayable.from_fco_summary(response.fco_summary)


class CompatBaseDataSource(BaseDataSource):
    @sdk_public_method
    def preview(self, limit: int = 10) -> pd.DataFrame:
        """
        Deprecated.
        Shows a preview of the data source's data from its batch data source.


        :param limit: (default=10) The number of rows to preview.
        :return: A pandas DataFrame containing a preview of data.
        """
        logger.warning(
            "Deprecated. Use the 'get_dataframe' method instead to data from your data source. See the api reference for this data source type, example: https://docs.tecton.ai/api-reference/stubs/tecton.interactive.BatchDataSource.html#tecton.interactive.BatchDataSource.get_dataframe"
        )

        return self.get_dataframe().to_spark().limit(limit).toPandas()

    @sdk_public_method
    def dataframe(self) -> DataFrame:
        """
        Deprecated.
        Returns this data source's data as a Spark DataFrame.

        :return: A Spark DataFrame containing the data source's data.
        """
        logger.warning(
            "Deprecated. Use the 'get_dataframe' method instead to data from your data source. See the api reference for this data source type, example: https://docs.tecton.ai/api-reference/stubs/tecton.interactive.BatchDataSource.html#tecton.interactive.BatchDataSource.get_dataframe"
        )

        return self.get_dataframe().to_spark()


class BatchDataSource(BaseDataSource):
    """
    BatchDataSource abstracts batch data sources.

    BatchFeatureViews and BatchWindowAggregateFeatureViews ingest data from BatchDataSources.
    """

    @classmethod
    def _fco_type_name_singular_snake_case(cls) -> str:
        return "batch_data_source"

    @classmethod
    def _fco_type_name_plural_snake_case(cls) -> str:
        return "batch_data_sources"


class StreamDataSource(BaseDataSource):
    """
    StreamDataSource is an abstraction data over streaming data sources.

    StreamFeatureViews and StreamWindowAggregateFeatureViews ingest data from StreamDataSources.

    A StreamDataSource contains a stream data source config, as well as a batch data source config for backfills.
    """

    @classmethod
    def _fco_type_name_singular_snake_case(cls) -> str:
        return "stream_data_source"

    @classmethod
    def _fco_type_name_plural_snake_case(cls) -> str:
        return "stream_data_sources"


class CompatBatchDataSource(CompatBaseDataSource):
    """
    BatchDataSource abstracts batch data sources.

    BatchFeatureViews and BatchWindowAggregateFeatureViews ingest data from BatchDataSources.
    """

    @classmethod
    def _fco_type_name_singular_snake_case(cls) -> str:
        return "batch_data_source"

    @classmethod
    def _fco_type_name_plural_snake_case(cls) -> str:
        return "batch_data_sources"


class CompatStreamDataSource(CompatBaseDataSource):
    """
    StreamDataSource is an abstraction data over streaming data sources.

    StreamFeatureViews and StreamWindowAggregateFeatureViews ingest data from StreamDataSources.

    A StreamDataSource contains a stream data source config, as well as a batch data source config for backfills.
    """

    @classmethod
    def _fco_type_name_singular_snake_case(cls) -> str:
        return "stream_data_source"

    @classmethod
    def _fco_type_name_plural_snake_case(cls) -> str:
        return "stream_data_sources"


@sdk_public_method
def get_data_source(name, workspace_name: Optional[str] = None) -> Union[BatchDataSource, StreamDataSource]:
    """
    Fetch an existing :class:`BatchDataSource` or :class:`StreamDataSource` by name.

    :param name: An unique name of the registered Data Source.

    :return: A :class:`BatchDataSource` or :class:`StreamDataSource` class instance.

    :raises TectonValidationError: if a data source with the passed name is not found.
    """
    if workspace_name == None:
        logger.warning(
            "`tecton.get_data_source('<name>')` is deprecated. Please use `tecton.get_workspace('<workspace_name>').get_data_source('<name>')` instead."
        )

    request = GetVirtualDataSourceRequest()
    request.name = name
    request.disable_legacy_response = True
    request.workspace = workspace_name or conf.get_or_none("TECTON_WORKSPACE")

    response = metadata_service.instance().GetVirtualDataSource(request)
    fco_container = FcoContainer(response.fco_container)
    ds_proto = fco_container.get_single_root()

    # this looks not very intuitive, why not use factory pattern and build the correct derived class instead of this logic?
    if not ds_proto:
        raise errors.DATA_SOURCE_NOT_FOUND(name)

    if ds_proto.fco_metadata.framework_version == FrameworkVersion.FWV5.value:
        if ds_proto.HasField("stream_data_source"):
            return StreamDataSource._create_from_proto(ds_proto, fco_container)
        else:
            return BatchDataSource._create_from_proto(ds_proto, fco_container)
    else:
        if ds_proto.HasField("stream_data_source"):
            return CompatStreamDataSource._create_from_proto(ds_proto, fco_container)
        else:
            return CompatBatchDataSource._create_from_proto(ds_proto, fco_container)
