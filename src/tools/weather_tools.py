import requests
import os

from dotenv import load_dotenv

load_dotenv()
# TODO: Pass the API key as an argument to the function instead (dependency injection)
API_KEY = os.getenv("WEATHER_API_KEY")

BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather(location: str) -> str:
    response = requests.get(BASE_URL, params={"key": API_KEY, "q": location})

    data = response.json()
    if response.status_code == 200:
        condition = data["current"]["condition"]["text"]
        return f"Weather in {location}: {condition}."
    else:
        return f"Error fetching weather data for {location}."


def get_temperature(location: str) -> str:
    response = requests.get(BASE_URL, params={"key": API_KEY, "q": location})
    data = response.json()
    if response.status_code == 200:
        temperature = data["current"]["temp_c"]
        return f"Temperature in {location}: {temperature}°C."
    else:
        return f"Error fetching temperature data for {location}."
