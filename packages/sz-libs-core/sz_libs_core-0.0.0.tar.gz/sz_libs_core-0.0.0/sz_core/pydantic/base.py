from enum import Enum, IntEnum
from typing import Any, TypeVar, ParamSpecKwargs

from pydantic import BaseModel as PydanticBaseModel
from pydantic import validator
from pydantic.main import ModelMetaclass  # noqa
from pydantic.fields import ModelField
from pydantic.generics import GenericModel

__all__ = (
    "BaseModel",
    "BaseAliasedModel",
    "BaseGenericModel",
    "PydanticModelT",
    "GenericPydanticModelT",
    "AnyPydanticModelT",
)


def _field_to_camel(field_name: str) -> str:
    words = field_name.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1::])


class OptionalPydanticModel(ModelMetaclass):
    def __new__(
        cls,
        name: str,
        bases: tuple[object],
        namespaces: dict[str, Any],
        **kwargs: ParamSpecKwargs
    ) -> "OptionalPydanticModel":
        annotations = namespaces.get("__annotations__", {})
        for base in bases:
            annotations.update(base.__annotations__)
        for field in annotations:
            if not field.startswith("__"):
                annotations[field] = annotations[field] | None
        namespaces["__annotations__"] = annotations
        return super().__new__(cls, name, bases, namespaces, **kwargs)


class BaseModel(PydanticBaseModel):
    class Config:
        json_encoders = {IntEnum: lambda enum: enum.name}

    @validator("*", pre=True, check_fields=False, allow_reuse=True, always=True)
    def enum_by_name(cls, v: Any, field: ModelField) -> Any:
        if issubclass(field.type_, Enum) and v in field.type_._member_names_:
            return field.type_[v]
        return v


class BaseAliasedModel(BaseModel):
    class Config:
        alias_generator = _field_to_camel
        allow_population_by_field_name = True


class BaseGenericModel(GenericModel, BaseModel):
    pass


class BaseAliasedGenericModel(BaseGenericModel, BaseAliasedModel):
    pass


PydanticModelT = TypeVar("PydanticModelT", bound=BaseModel)
GenericPydanticModelT = TypeVar("GenericPydanticModelT", bound=BaseGenericModel)
AnyPydanticModelT = TypeVar("AnyPydanticModelT", bound=BaseModel | BaseGenericModel)
