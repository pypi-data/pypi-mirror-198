from typing import Any, TypeAlias

from app.core.pydantic.base import PydanticModelT, BaseGenericModel

AriadneResult: TypeAlias = list[dict[str, Any]] | dict[str, Any]
PydanticResult: TypeAlias = BaseGenericModel | PydanticModelT
