from typing import AsyncGenerator
from httpx import AsyncClient


async def get_http_client() -> AsyncGenerator:
    async with AsyncClient() as client:
        yield client
