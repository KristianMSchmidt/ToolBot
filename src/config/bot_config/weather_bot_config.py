import os
from dotenv import load_dotenv
from src.tools.weather_tools import get_current_weather, get_todays_weather_alerts

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

# System instruction for the weather chatbot
SYSTEM_INSTRUCTION = (
    "You are an assistant specializing in questions about the current weather, "
    "such as temperature, wind, or what to wear based on current conditions. "
    "Your expertise is limited to providing details about the current weather "
    "for various locations. If a question is unrelated to the current weather, "
    "such as a forecast for tomorrow, politely inform the user that you can "
    "only assist with current weather-related topics."
)

# Greeting message displayed to the user
GREETING_MESSAGE = """
🌦️ Hi! Welcome to the Weather Chatbot! 🌟
I'm here to help you with all your weather-related questions.

Here are some things you can ask me:
- 'What is the weather like in Copenhagen?'
- 'What should I wear in Athens today?'
- 'What tires should I use in Helsinki today?'
- 'What is the temperature in China's 5 biggest cities today?'

💡 Type 'exit' at any time to quit the chat.
Let's get started! 🌈
"""

TOOLS = [
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
