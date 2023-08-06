import json
from typing import TYPE_CHECKING, Any
from ipaddress import IPv4Address

from consul import Consul
from pydantic import Extra, Field, root_validator

from sz_core.configs.base import BaseSettings

if TYPE_CHECKING:
    from pydantic.typing import DictStrAny

__all__ = ("BaseConsulSettings",)


class BaseConsulSettings(BaseSettings):

    CONSUL_HOST: IPv4Address | str
    CONSUL_PORT: int = Field(..., ge=1, le=65535)
    CONSUL_KV_PATH: str

    _consul_client: Consul | None = None

    class Config:
        extra = Extra.allow

    @root_validator(pre=True, allow_reuse=True, skip_on_failure=True)
    @classmethod
    def consul_getter(cls, values: "DictStrAny") -> "DictStrAny":
        consul_host = values.get("CONSUL_HOST")
        consul_port = values.get("CONSUL_PORT")
        if not (consul_host or consul_port):
            return values

        if not cls._consul_client:
            cls._consul_client = Consul(
                host=consul_host,
                port=consul_port,
            )

        _, result = cls._consul_client.kv.get(values.get("CONSUL_KV_PATH"))
        data: dict[str, Any] = json.loads(result["Value"])
        data.update(values)

        return data
