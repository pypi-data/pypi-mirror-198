"""Handle schema errors."""

from typing import Dict, List, Union

from pandera.errors import SchemaError, SchemaErrorReason


class SchemaErrorHandler:
    """Handler for SchemaError objects during validation."""

    def __init__(self, lazy: bool) -> None:
        """Initialize SchemaErrorHandler.

        :param lazy: if True, lazily evaluates schema checks and stores
            SchemaError objects. Otherwise raise a SchemaError immediately.
        """
        self._lazy = lazy
        self._collected_errors = []  # type: ignore

    @property
    def lazy(self) -> bool:
        """Whether or not the schema error handler raises errors immediately."""
        return self._lazy

    def collect_error(
        self,
        reason_code: SchemaErrorReason,
        schema_error: SchemaError,
        original_exc: BaseException = None,
    ):
        """Collect schema error, raising exception if lazy is False.

        :param reason_code: string representing reason for error
        :param schema_error: ``SchemaError`` object.
        """
        if not self._lazy:
            raise schema_error from original_exc

        # delete data of validated object from SchemaError object to prevent
        # storing copies of the validated DataFrame/Series for every
        # SchemaError collected.
        del schema_error.data
        schema_error.data = None

        self._collected_errors.append(
            {
                "reason_code": reason_code,
                "error": schema_error,
            }
        )

    @property
    def collected_errors(self) -> List[Dict[str, Union[SchemaError, str]]]:
        """Retrieve SchemaError objects collected during lazy validation."""
        return self._collected_errors
