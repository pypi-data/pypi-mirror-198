from typing import Type

from fastapi import Request, Response, status
from pydantic import parse_raw_as
from fastapi.exceptions import RequestValidationError
from sz_core.enums.errors import ErrorCode, ErrorType
from sz_core.fastapi.schemas.error_wrapper import FieldsErrors, AbsErrorWrapper
from sz_core.fastapi.schemas.response_wrapper import ResponseWrapper

from .base import ExceptionHandler, build_response


def __format_errors_to_text(exc: RequestValidationError) -> str:
    return "\n".join(
        [f"{'.'.join(e.loc_tuple())}: {e.exc};" for e in exc.raw_errors]  # type: ignore
    )


def __format_errors_to_list(exc: RequestValidationError) -> list[FieldsErrors]:
    return parse_raw_as(list[FieldsErrors], exc.json())


def build_validation_exception_handler(
    error_wrapper: Type[AbsErrorWrapper],
    as_json: bool = True,
) -> ExceptionHandler:
    def validation_exception_handler(
        _: Request,
        exc: RequestValidationError,
    ) -> Response:
        error = error_wrapper(
            type=ErrorType.VALIDATION,
            code=ErrorCode.NOT_VALID_DATA,
        )
        if as_json:
            error.msg = "Request validation error"
            error.fields = __format_errors_to_list(exc)
        else:
            error.msg = __format_errors_to_text(exc)
        return build_response(
            content=ResponseWrapper[None].make_error(error).json(by_alias=True),
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )

    return validation_exception_handler  # type: ignore
