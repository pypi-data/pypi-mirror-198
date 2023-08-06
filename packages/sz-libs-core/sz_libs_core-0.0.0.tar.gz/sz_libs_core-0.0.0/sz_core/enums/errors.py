from enum import Enum, auto
from typing import TypeVar

from .base import StringAutoEnum

ErrorTypeT = TypeVar("ErrorTypeT", bound=Enum)
ErrorCodeT = TypeVar("ErrorCodeT", bound=Enum)


class ErrorType(StringAutoEnum):
    BASE = auto()
    VALIDATION = auto()


class ErrorCode(StringAutoEnum):
    UNKNOWN = auto()
    BASE_ERROR_CODE = auto()
    NOT_VALID_DATA = auto()
