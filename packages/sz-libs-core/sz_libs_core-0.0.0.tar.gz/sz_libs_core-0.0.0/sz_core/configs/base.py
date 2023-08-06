from typing import Any

from pydantic import Json, Field
from pydantic import BaseSettings as BasePydanticSettings
from sz_core.enums.env import ENVEnum

__all__ = ("BaseSettings",)


class BaseSettings(BasePydanticSettings):
    """Base project settings"""

    # ####### Main application settings #########
    ENV: ENVEnum = Field(ENVEnum.LOCAL)
    DEBUG: bool = Field(True)
    SERVICE_NAME: str = Field("")
    VERSION: str = Field("local")

    # ################ Logging ##################
    LOGGING_LEVEL: str = Field("info")
    LOGGING_SERIALIZE: bool = Field(False)

    SENTRY_URL: str | None = Field()

    # ################ RestAPI ##################

    # CORS origins
    CORS_ORIGINS: list[str] = Field(["*"])

    class Config:
        env_file = ".env"

        @classmethod
        def parse_env_var(cls: Json, field_name: str, raw_val: str) -> Any:
            if field_name == "CORS_ORIGINS":
                return [x.strip() for x in raw_val.split(",")]
            return cls.json_loads(raw_val)
