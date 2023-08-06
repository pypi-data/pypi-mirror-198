from typing import AsyncGenerator
from contextlib import asynccontextmanager

from httpx import AsyncClient
from fastapi import FastAPI


@asynccontextmanager
async def async_client(
    app: FastAPI, headers: dict | None = None
) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
        app=app,
        verify=False,
        base_url="http://test",
        http2=True,
        headers=headers or {},
    ) as ac:
        yield ac
