from tools.weather_tools import get_weather, get_temperature

TOOL_CONFIG = [
    {
        "name": "get_weather",
        "description": "Retrieve the current weather for a specific location. Use this to provide weather updates when requested.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The name of the location (e.g., city or town) for which the weather is needed.",
                },
            },
            "required": ["location"],
            "additionalProperties": False,
        },
        "function": get_weather,
    },
    {
        "name": "get_temperature",
        "description": "Retrieve the current temperature for a specific location. Use this to answer temperature-specific questions.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The name of the location (e.g., city or town) for which the temperature is needed.",
                },
            },
            "required": ["location"],
            "additionalProperties": False,
        },
        "function": get_temperature,
    },
]
