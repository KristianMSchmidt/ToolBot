from src.tools.smk_tools.get_artworks_by_object_number import (
    get_artworks_by_object_numbers,
)
from src.tools.smk_tools.get_artworks_by_search import get_artworks_by_search
from src.bot_config.base_bot_config import BotConfig

# SMK bot configuration
smk_bot_config = BotConfig(
    name="SMK Chatbot",
    system_instruction=(
        "You are an assistant specializing in questions about the digital art collection at SMK. You are careful to use the provided tools effeciently, e.g. whhen you need info about 2 or more artworks, you only use the tool to get this information once, by providing all the parameters in a list."
    ),
    greeting_message="""
    Hi! Welcome to the SMK Chatbot!
    """,
    tool_config=[
        {
            "name": get_artworks_by_object_numbers.__name__,
            "description": (
                "Fetch information about one or more artworks from the SMK collection using their object numbers. "
                "Provide an array of object numbers for multiple artworks."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "object_numbers": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "description": "An artwork's unique object number.",
                        },
                        "description": "A list of unique object numbers for the artworks.",
                    }
                },
                "required": ["object_numbers"],
                "additionalProperties": False,
            },
            "function": get_artworks_by_object_numbers,
        },
        {
            'name': get_artworks_by_search.__name__,
            'description': (
                "Call this if the user wants to search in the SMK art collection."
            ),
            'parameters': {
                'type': 'object',
                'properties': {
                    'search_words': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'description': "A keyword to use in the search. Multiple keywords narrow down the search results.",
                        },
                        'description': "A list of keywords to search for artworks in the SMK collection.",
                    },
                    'creator_nationality': {
                        'type': 'string',
                        "enum": [
                            "dansk",
                            "svensk",
                            "norsk",
                            "tysk",
                            "engelsk",
                            "fransk",
                            "hollandsk",
                            "nederlansk",
                            "spansk",
                            "italiensk",
                        ],
                        'description': 'The nationality of the artist (such as "svensk" eller "nederlandsk"). Should be in Danish',
                    },
                },
                'required': ['search_words'],
                'additionalProperties': False,
            },
            'function': get_artworks_by_search,
        },
    ],
)
