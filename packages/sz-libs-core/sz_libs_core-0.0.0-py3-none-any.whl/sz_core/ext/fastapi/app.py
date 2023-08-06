from typing import Any, Type

from fastapi import FastAPI, APIRouter
from sz_core.logging import logger
from sz_core.enums.env import ENVEnum
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from sz_core.configs.base import BaseSettings
from sz_core.enums.errors import ErrorCode, ErrorType
from fastapi.middleware.cors import CORSMiddleware
from sz_core.exceptions.base import BaseAbsAppException
from sz_core.fastapi.schemas.error_wrapper import ErrorWrapper
from sz_core.fastapi.handlers.base_error_handlers import (
    ExceptionHandler,
    build_base_exception_handler,
)
from sz_core.fastapi.handlers.validation_error_handlers import (
    build_validation_exception_handler,
)


class FastAPIBuilder:

    main_app_exception: Type[BaseAbsAppException] = BaseAbsAppException
    docs_servers: list[dict[str, str]] | None = None
    openapi_schema_url: str = "/openapi.json"
    swagger_url: str = "/docs"
    redoc_url: str = "/redoc"
    hide_docs_on_production: bool = True
    default_version: str = "latest"

    settings: BaseSettings
    logger: Any = logger

    base_error_handler: ExceptionHandler = build_base_exception_handler(
        error_wrapper=ErrorWrapper,
        base_app_exception=BaseAbsAppException[ErrorType, ErrorCode],
    )
    validation_error_handler: ExceptionHandler = build_validation_exception_handler(
        error_wrapper=ErrorWrapper,
        as_json=True,
    )

    root_router: APIRouter
    root_url_prefix: str = ""

    def __init__(self) -> None:
        raise NotImplementedError(
            "FastAPIBuilder does not support create the factory instance."
            " To get a FastAPI instance, use the build method"
        )

    @classmethod
    def checks(cls) -> None:
        exceptions: list[Exception] = []
        settings = getattr(cls, "settings", None)
        if not isinstance(settings, BaseSettings):
            exceptions.append(
                TypeError(
                    f"Settings must be instance of subclass BaseSettings."
                    f" Current: {settings}"
                )
            )
        root_router = getattr(cls, "root_router", None)
        if not isinstance(root_router, APIRouter):
            exceptions.append(
                TypeError(
                    f"Root router must be instance of subclass FastAPI APIRouter."
                    f" Current: {root_router}"
                )
            )
        if exceptions:
            raise ExceptionGroup(f"{cls.__name__} checks failed", exceptions)  # type: ignore[name-defined]  # noqa: E501

    @classmethod
    def init_middlewares(cls, fastapi: FastAPI) -> FastAPI:
        fastapi.add_middleware(
            CORSMiddleware,
            allow_origins=cls.settings.CORS_ORIGINS,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        return fastapi

    @classmethod
    def init_exception_handlers(cls, fastapi: FastAPI) -> FastAPI:
        fastapi.add_exception_handler(
            RequestValidationError, cls.validation_error_handler
        )
        fastapi.add_exception_handler(HTTPException, cls.base_error_handler)
        fastapi.add_exception_handler(BaseAbsAppException, cls.base_error_handler)
        return fastapi

    @classmethod
    def init_routes(cls, fastapi: FastAPI) -> FastAPI:
        root_prefix = cls.root_url_prefix or ""
        fastapi.include_router(cls.root_router, prefix=root_prefix)
        return fastapi

    @classmethod
    def build(cls) -> FastAPI:
        cls.checks()

        hide_docs = cls.hide_docs_on_production and cls.settings.ENV == ENVEnum.PROD
        print(hide_docs, cls.openapi_schema_url, cls.swagger_url, cls.redoc_url)

        fastapi = FastAPI(
            title=f"{cls.settings.SERVICE_NAME.capitalize()} service",
            servers=cls.docs_servers,
            debug=cls.settings.DEBUG,
            openapi_url=cls.openapi_schema_url if not hide_docs else None,
            docs_url=cls.swagger_url if not hide_docs else None,
            redoc_url=cls.redoc_url if not hide_docs else None,
            version=cls.settings.VERSION or cls.default_version,
        )

        fastapi.logger = logger  # type: ignore

        fastapi = cls.init_exception_handlers(fastapi)
        fastapi = cls.init_middlewares(fastapi)
        fastapi = cls.init_routes(fastapi)

        return fastapi
