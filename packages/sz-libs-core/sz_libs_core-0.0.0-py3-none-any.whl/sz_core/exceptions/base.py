from typing import Generic

from sz_core.enums.errors import ErrorCode, ErrorType, ErrorCodeT, ErrorTypeT


class BaseAbsAppException(Exception, Generic[ErrorTypeT, ErrorCodeT]):
    """Base domain error."""

    type: ErrorTypeT = ErrorType.BASE  # type: ignore # noqa: A003
    code: ErrorCodeT = ErrorCode.BASE_ERROR_CODE  # type: ignore
    msg: str = "Unknown error"
    http_status: int = 400

    def __init__(
        self,
        msg: str | None = None,
        error_type: ErrorTypeT | None = None,
        code: ErrorCodeT | None = None,
        http_status: int | None = None,
    ):
        if error_type:
            self.type = error_type
        if code:
            self.code = code
        if msg:
            self.msg = msg
        if http_status:
            self.http_status = http_status

    def __str__(self) -> str:
        return f"{self.type} - {self.msg} ({self.code})"
