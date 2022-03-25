from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from httpx import AsyncClient

from app.db.cache import cache_exists, cache_request, get_cached_request
from app.deps import get_http_client
from app.services import get_data

router = APIRouter()


@router.get('/{city}/')
async def get_city_info(city: str, client: AsyncClient = Depends(get_http_client)) -> ORJSONResponse:
    """Returns weather data for city and the last article in NewYorkTimes where city is mentioned.

    Args:
        city (str): City name.
        client (AsyncClient, optional): Async httpx client. Defaults to Depends(get_http_client).

    Returns:
        ORJSONResponse: Json response, handled by orjson.
    """
    
    if await cache_exists(city):
        return ORJSONResponse(await get_cached_request(city))
    
    data = await get_data(city, client)
    await cache_request(city, data)
    return ORJSONResponse(data)
