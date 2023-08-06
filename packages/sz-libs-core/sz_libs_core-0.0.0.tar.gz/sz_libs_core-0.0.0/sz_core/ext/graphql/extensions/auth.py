from typing import Any, TypeVar, Callable, Awaitable, cast
from functools import wraps

from graphql import GraphQLResolveInfo
from ariadne.types import Extension
from sz_core.pydantic.base import AnyPydanticModelT

__all__ = (
    "AuthExtension",
    "required_auth",
)

DecoratedFunc = TypeVar("DecoratedFunc", bound=Callable[..., Awaitable[Any]])


class AuthExtension(Extension):
    def request_started(  # type: ignore
        self, context: dict[str, Any]
    ) -> dict[str, Any]:
        headers = dict(context["request"].headers)
        access_token = headers.get("authorization")
        if not access_token:
            return context
        # TODO: Temp user id. In future passed User struct from JWT
        context["user"] = {"uid": access_token}
        return context


def required_auth(
    user_model: AnyPydanticModelT,
) -> Callable[[DecoratedFunc], DecoratedFunc]:
    def decorator(func: DecoratedFunc) -> DecoratedFunc:
        @wraps(func)
        async def wrap(
            _: None, info: GraphQLResolveInfo, *args: Any, **params: Any
        ) -> Awaitable[Any]:
            # TODO: Temp user id. In future passed User struct from JWT
            user = info.context.get("user", {})
            params.setdefault("user", user_model.parse_obj(user))
            return await func(_, info, *args, **params)

        return cast(DecoratedFunc, wrap)

    return decorator
