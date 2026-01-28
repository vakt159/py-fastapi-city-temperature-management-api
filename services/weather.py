import os

import httpx

URL = "http://api.weatherapi.com/v1/current.json?"
KEY = os.getenv("API_KEY")


async def get_weather(city_name: str) -> str:
    if not KEY:
        return "API_KEY is missing"
    async with httpx.AsyncClient() as client:
        response = await client.get(URL + f"key={KEY}&q={city_name}")
    data = response.json()
    temp = data["current"]["temp_c"]
    return temp
