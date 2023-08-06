from typing import Type

from fastapi import Request, Response
from sz_core.exceptions.base import BaseAbsAppException
from sz_core.fastapi.schemas.error_wrapper import AbsErrorWrapper
from sz_core.fastapi.schemas.response_wrapper import ResponseWrapper

from .base import ExceptionHandler, build_response


def build_base_exception_handler(
    error_wrapper: Type[AbsErrorWrapper],
    base_app_exception: Type[BaseAbsAppException],
) -> ExceptionHandler:
    def base_exception_handler(_: Request, exc: Exception) -> Response:
        if not isinstance(exc, base_app_exception):
            exc = base_app_exception(msg=str(exc))
        response_wrapper = ResponseWrapper[None].make_error(
            error=error_wrapper(
                type=exc.type,
                code=exc.code,
                msg=exc.msg if exc.msg else "Internal server error!",
            )
        )
        return build_response(
            content=response_wrapper.json(by_alias=True), status_code=exc.http_status
        )

    return base_exception_handler
