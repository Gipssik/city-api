from typing import Optional
from pydantic import BaseModel


class Weather(BaseModel):
    main: str
    description: str


class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: float
    humidity: float
    

class Wind(BaseModel):
    speed: float
    deg: float
    gust: Optional[float] = None
    

class Clouds(BaseModel):
    all: float
    
    
class Sys(BaseModel):
    sunrise: str
    sunset: str
    
    
class WeatherData(BaseModel):
    country: str
    city_name: str
    weather: Weather
    main: Main
    visibility: float
    wind: Wind
    clouds: Clouds
    weather_datetime: str
    sys: Sys
