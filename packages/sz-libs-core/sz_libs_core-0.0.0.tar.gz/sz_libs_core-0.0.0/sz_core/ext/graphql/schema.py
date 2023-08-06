import aiohttp
import aiofiles
from ariadne import SchemaBindable, gql
from graphql import GraphQLSchema
from pydantic import FileUrl, HttpUrl
from sz_core.logging import logger
from ariadne.contrib.federation.schema import make_federated_schema

__all__ = ("get_schema",)


async def _load_scheme_from_file(url: FileUrl) -> str:
    async with aiofiles.open(url.path or "", mode="r") as f:
        return await f.read()


async def _load_scheme_from_url(url: HttpUrl) -> str:
    user = url.user
    password = url.password
    if not user or not password:
        raise ValueError("User or password for graphql scheme url is not defined")
    clean_url = f"{url.scheme}://{url.host}{url.path}"
    async with aiohttp.ClientSession() as c:
        auth = aiohttp.BasicAuth(user, password)
        async with c.get(clean_url, auth=auth) as resp:
            if resp.status != 200:
                logger.critical(
                    f'Error loading scheme with code "{resp.status}"'
                    f"by url: {clean_url}"
                )
                raise ValueError(await resp.text())
            return await resp.text()


async def get_schema(
    scheme_url: FileUrl | HttpUrl,
    *binds: SchemaBindable | list[SchemaBindable],
) -> GraphQLSchema:
    gql_schema = getattr(get_schema, "__schema", None)
    if not gql_schema:
        if isinstance(scheme_url, FileUrl):
            schema = await _load_scheme_from_file(scheme_url)
        elif isinstance(scheme_url, HttpUrl):
            schema = await _load_scheme_from_url(scheme_url)
        else:
            raise ValueError("Incorrect graphql scheme url. Scheme cannot load.")
        gql_schema = make_federated_schema(
            gql(schema),
            *binds,
        )
        setattr(get_schema, "__schema", gql_schema)
    return gql_schema
