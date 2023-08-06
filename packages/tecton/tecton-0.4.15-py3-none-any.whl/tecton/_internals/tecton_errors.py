class TectonAPIValidationError(ValueError):
    """
    Exception that indicates a problem in validating user inputs against
    the data in the system. Typically recoverable by the user.
    """


class TectonNotFoundError(Exception):
    """
    Exception that indicates that the user's request cannot be found in the system.
    """


class TectonAPIInaccessibleError(Exception):
    """
    Exception that indicates a problem connecting to Tecton cluster.
    """


class FailedPreconditionError(Exception):
    """
    Exception that indicates some prequisite has not been met (e.g the CLI/SDK needs to be updated).
    """


class InvalidDatabricksTokenError(Exception):
    """
    Exception that indicates user's databricks token is invalid.
    """
