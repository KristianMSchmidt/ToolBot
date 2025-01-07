import os
from dotenv import load_dotenv
from src.tools.weather_tools import get_current_weather, get_todays_weather_alerts

load_dotenv()


API_KEY = os.getenv("WEATHER_API_KEY")

TOOL_CONFIG = [
    {
        "name": "get_current_weather",
        "description": (
            "Retrieve the details of the current weather for a specific location. "
            "Use this to answer general questions about current weather (including "
            "what to wear or how to behave given the weather)."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": (
                        "The name of the location (e.g., city or town) for which "
                        "the weather details is needed."
                    ),
                },
            },
            "required": ["location"],
            "additionalProperties": False,
        },
        "function": lambda location: get_current_weather(location, API_KEY),
    },
    {
        "name": "get_todays_weather_alerts",
        "description": (
            "Retrieve weather alerts for today for a specific location. Use this to "
            "provide users with information about weather-related alerts for the day."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": (
                        "The name of the location (e.g., city or town) for which "
                        "the weather alerts are needed."
                    ),
                },
            },
            "required": ["location"],
            "additionalProperties": False,
        },
        "function": lambda location: get_todays_weather_alerts(API_KEY, location),
    },
]
