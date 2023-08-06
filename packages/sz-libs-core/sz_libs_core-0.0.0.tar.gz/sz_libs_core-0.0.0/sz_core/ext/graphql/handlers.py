import json
from typing import Any

from ariadne import format_error
from graphql import GraphQLError
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from ariadne.asgi.handlers import GraphQLHTTPHandler
from sz_core.exceptions.base import BaseAbsAppException
from sz_core.encoders.pydantic import PydanticJsonableEncoder


class CustomJSONResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=None,
            cls=PydanticJsonableEncoder,
            separators=(",", ":"),
        ).encode("utf-8")


class CustomGraphQLHTTPHandler(GraphQLHTTPHandler):
    async def create_json_response(
        self, request: Request, result: dict[str, Any], success: bool
    ) -> Response:
        status_code = 200 if success else 400
        return CustomJSONResponse(result, status_code=status_code)


def _get_app_exception(error: GraphQLError) -> BaseAbsAppException:
    if isinstance(error.original_error, BaseAbsAppException):
        exc = error.original_error
    else:
        exc = BaseAbsAppException()
        if error.original_error:
            exc.__traceback__ = error.original_error.__traceback__
    return exc


def _get_error_extension(exc: BaseAbsAppException) -> dict[str, str]:
    return {
        "msg": exc.msg,
        "type": exc.type.value,
        "code": exc.code.value,
    }


def error_formatter(error: GraphQLError, debug: bool = False) -> dict[str, Any]:
    result = format_error(error, debug)
    exc = _get_app_exception(error)
    if "extensions" not in result:
        result["extensions"] = {}
    result["extensions"]["info"] = _get_error_extension(exc)
    result["message"] = exc.msg
    return result
