from typing import TypeVar, Callable, Awaitable

from fastapi import Request

DEPENDENCY_RETURN_T = TypeVar("DEPENDENCY_RETURN_T")


def mock_dependency_fabric(
    returns: DEPENDENCY_RETURN_T,
) -> Callable[[Request], Awaitable[DEPENDENCY_RETURN_T]]:
    async def mock_dep(_: Request) -> DEPENDENCY_RETURN_T:
        return returns

    return mock_dep
