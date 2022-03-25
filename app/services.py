import logging
import os
from typing import Any

from fastapi import HTTPException, status
from httpx import AsyncClient

from app.utils import validate_nyt_data, validate_weather_data

logger = logging.getLogger(__name__)


async def get_weather_data(city: str, client: AsyncClient) -> dict[str, Any]:
    """Returns weather data for city.

    Args:
        city (str): City name.
        client (AsyncClient): Async httpx client.

    Raises:
        HTTPException: If city is not found.

    Returns:
        dict[str, Any]: Weather data.
    """
    
    logger.info(f'Start gathering weather for city {city}')
    
    w_api_key = os.getenv('WEATHER_API_KEY')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={w_api_key}&units=metric'
    
    response = await client.get(url=url)
    response_json: dict[str, Any] = response.json()
    
    if response.status_code == 404:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=response_json['message']
        )
    
    weather = validate_weather_data(response_json)
    
    logger.info(f'Got weather for city {city}')
    return weather


async def get_nyt_data(city: str, client: AsyncClient) -> dict[str, Any]:
    """Returns last article in NewYorkTimes where city is mentioned.

    Args:
        city (str): City name.
        client (AsyncClient): Async httpx client.

    Returns:
        dict[str, Any]: Last article in NewYorkTimes where city is mentioned.
    """
    
    logger.info(f'Start gathering NYT for city {city}')
    
    nyt_api_key = os.getenv('NYT_API_KEY')
    query = f'{city} AND document_type: ("article")'
    url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?fq={query}&api-key={nyt_api_key}'
    
    response = await client.get(url=url)
    response_json: dict[str, Any] = validate_nyt_data(response.json())
    
    logger.info(f'Got NYT for city {city}')
    return response_json


async def get_data(city: str, client: AsyncClient) -> dict[str, dict]:
    """Returns weather data and last article in NewYorkTimes where city is mentioned.

    Args:
        city (str): City name.
        client (AsyncClient): Async httpx client.

    Returns:
        dict[str, dict]: Weather data and last article in NewYorkTimes where city is mentioned.
    """
    
    weather = await get_weather_data(city, client)
    nyt = await get_nyt_data(weather['city_name'], client)
    
    data = {
        'weather': weather,
        'nyt': nyt
    }
    return data