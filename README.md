# city-api

API to get city's weather and last mentioned article in NYT.

## Requirements

* Python 3.10+

### Local development

First, create a `.env` file with the following content:
```bash
WEATHER_API_KEY=<YOUR_WEATHER_API_KEY>
NYT_API_KEY=<YOUR_NYT_API_KEY>
REDIS_HOST=<YOUR_REDIS_HOST>
REDIS_PORT=<YOUR_REDIS_PORT>
REDIS_DB=<YOUR_REDIS_DB>
REDIS_PASSWORD=<YOUR_REDIS_PASSWORD>
```

Also, you need to set your REDIS_PASSWORD in docker-compose.yml file on line 31.

Then, start the stack with Docker Compose:
```bash
# Build services
docker-compose build

# Create and start containers
docker-compose up -d
```

Now you can open your browser and interact with these URLs:
* Automatic interactive documentation with Swagger UI: http://localhost:8080/docs
* Alternative automatic documentation with ReDoc: http://localhost:8080/redoc
