import logging
from typing import Any

import orjson

from app.db.redis import r

logger = logging.getLogger(__name__)


async def cache_request(city: str, data: dict[str, Any]):
    """Cash request in redis.

    Args:
        city (str): City name.
        data (dict[str, Any]): Data to cache.
    """
    
    await r.set(city, orjson.dumps(data))
    await r.expire(city, 60 * 15)
    logger.info(f'Cached request for city {city}')
    
    
async def cache_exists(city: str) -> bool:
    """Check if city cache exists.

    Args:
        city (str): City name.

    Returns:
        bool: Whether city cache exists.
    """
    
    return await r.exists(city)
    
    
async def get_cached_request(city: str) -> dict[str, Any]:
    """Returns cached request by city name.

    Args:
        city (str): City name.

    Returns:
        dict[str, Any]: Cached request.
    """
    
    data = await r.get(city)
    logger.info(f'Got cached request for city {city}')
    return orjson.loads(data)
