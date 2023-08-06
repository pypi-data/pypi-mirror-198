import json
from typing import Callable, Awaitable, TypeAlias, ParamSpecArgs, ParamSpecKwargs
from functools import wraps

from sz_core.encoders.pydantic import PydanticJsonableEncoder
from sz_core.ext.graphql.typing import AriadneResult, PydanticResult

DecoratedFunc: TypeAlias = Callable[
    ..., Awaitable[list[PydanticResult] | PydanticResult]
]
AriadneResolver: TypeAlias = Callable[..., Awaitable[AriadneResult]]

__all__ = ("pydantic_return",)


def _pydantic_to_dict_with_json(
    models: list[PydanticResult] | PydanticResult,
) -> AriadneResult:
    return json.loads(json.dumps(models, cls=PydanticJsonableEncoder))


def pydantic_return(f: DecoratedFunc) -> AriadneResolver:
    @wraps(f)
    async def wrapper(*args: ParamSpecArgs, **kwargs: ParamSpecKwargs) -> AriadneResult:
        return _pydantic_to_dict_with_json(await f(*args, **kwargs))

    return wrapper
