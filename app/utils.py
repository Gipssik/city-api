import datetime
from re import I
from typing import Any

import pycountry

from app.schemas import WeatherData, NewYorkTimes


def validate_weather_data(data: dict[str, Any]) -> dict[str, Any]:
    """Validates weather data.

    Args:
        data (dict[str, Any]): Weather data.

    Returns:
        dict[str, Any]: Validated weather data.
    """
    
    data['weather'] = data['weather'][0]
    
    data['sys']['sunrise'] = str(datetime.datetime.fromtimestamp(data['sys']['sunrise']))
    data['sys']['sunset'] = str(datetime.datetime.fromtimestamp(data['sys']['sunset']))
    data['country'] = pycountry.countries.get(alpha_2=data['sys']['country']).name
    
    data['city_name'] = data['name']
    
    data['weather_datetime'] = str(datetime.datetime.fromtimestamp(data['dt']))
    
    data_obj = WeatherData(**data)
    
    return data_obj.dict(exclude_unset=True)


def validate_nyt_data(data: dict[str, Any]) -> dict[str, str]:
    """Validates NewYorkTimes data.

    Args:
        data (dict[str, Any]): NewYorkTimes data.

    Returns:
        dict[str, str]: Validated NewYorkTimes data.
    """
    
    try:
        data = data['response']['docs'][0]
    except IndexError:
        return {'message': 'no posts with this city'}
    
    data['headline'] = data['headline']['main']
    
    data_obj = NewYorkTimes(**data)
    
    return data_obj.dict()
