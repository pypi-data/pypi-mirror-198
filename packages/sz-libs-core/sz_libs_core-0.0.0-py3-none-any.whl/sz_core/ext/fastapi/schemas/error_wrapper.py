from abc import ABC
from enum import Enum

from pydantic import BaseModel
from sz_core.exceptions.base import ErrorCode, ErrorType


class FieldsErrors(BaseModel):
    loc: list[str]
    msg: str
    type: str


class AbsErrorWrapper(BaseModel, ABC):
    type: Enum
    code: Enum
    msg: str = ""
    fields: list[FieldsErrors] | None = None


class ErrorWrapper(AbsErrorWrapper):
    type: ErrorType = ErrorType.BASE  # noqa: A003
    code: ErrorCode = ErrorCode.BASE_ERROR_CODE
    msg: str = ""
    fields: list[FieldsErrors] | None = None
