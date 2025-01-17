import os
from dotenv import load_dotenv
from src.tools.weather_tools import get_current_weather, get_todays_weather_alerts
from src.bot_config.base_bot_config import BotConfig

# Load environment variables
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

if not API_KEY:
    raise EnvironmentError("Missing required environment variable: WEATHER_API_KEY")

weather_bot_config = BotConfig(
    name="Weather Chatbot",
    system_instruction=(
        "You are an assistant specializing in questions about the current weather, "
        "such as temperature, wind, or what to wear based on current conditions. "
        "Your expertise is limited to providing details about the current weather "
        "for various locations (you can't do forecasting)."
    ),
    greeting_message="""
    🌦️ Hi! Welcome to the Weather Chatbot! 🌟
    I'm here to help you with all your weather-related questions.

    Here are some things you can ask me:
    - 'What is the weather like in Copenhagen?'
    - 'What should I wear in Athens today?'
    - 'What tires should I use in Helsinki today?'
    - 'What is the temperature in China's 5 biggest cities today?'

    💡 Type 'exit' at any time to quit the chat.
    Let's get started! 🌈
    """,
    tool_config=[
        {
            "name": get_current_weather.__name__,
            "description": get_current_weather.__doc__,
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "Name of the location (e.g., city or town).",
                    }
                },
                "required": ["location"],
                "additionalProperties": False,
            },
            "function": lambda location: get_current_weather(location, API_KEY),
        },
        {
            "name": get_todays_weather_alerts.__name__,
            "description": get_todays_weather_alerts.__doc__,
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "Name of the location (e.g., city or town).",
                    }
                },
                "required": ["location"],
                "additionalProperties": False,
            },
            "function": lambda location: get_todays_weather_alerts(API_KEY, location),
        },
    ],
)
