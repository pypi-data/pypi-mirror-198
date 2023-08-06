from typing import Callable, TypeAlias

from fastapi import Request, Response, status

ExceptionHandler: TypeAlias = Callable[[Request, Exception], Response]


def build_response(
    content: str,
    status_code: int = status.HTTP_200_OK,
    media_type: str = "application/json",
) -> Response:
    return Response(status_code=status_code, content=content, media_type=media_type)
