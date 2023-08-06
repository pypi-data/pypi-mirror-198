from typing import Generic, TypeVar

from pydantic import Field
from pydantic.generics import GenericModel

from .error_wrapper import AbsErrorWrapper
from .response_paging import ResponsePagingByPage

ResponseWrapperDataT = TypeVar("ResponseWrapperDataT")


class ResponseWrapper(GenericModel, Generic[ResponseWrapperDataT]):
    """Global reponse scheme"""

    data: ResponseWrapperDataT | None = Field(None, description="Response data")
    is_success: bool = Field(True, description="Success flag")

    pagination: ResponsePagingByPage | None = Field(
        None, description="Pagination object (if available)"
    )
    error: AbsErrorWrapper | None = Field(
        None,
        description="Error details (if request not successed)",
    )

    @classmethod
    def make_success(
        cls,
        data: ResponseWrapperDataT | None,
        pagination: ResponsePagingByPage | None = None,
    ) -> "ResponseWrapper[ResponseWrapperDataT]":
        """Return ResponseWrapper with passed data for successfully response."""
        return cls(
            data=data,
            pagination=pagination,
            is_success=True,
        )

    @classmethod
    def make_error(
        cls, error: AbsErrorWrapper | None = None
    ) -> "ResponseWrapper[ResponseWrapperDataT]":
        """Return ResponseWrapper with passed error for response with fails."""
        return cls(
            data=None,
            is_success=False,
            error=error,
        )
