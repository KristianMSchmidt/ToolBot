from src.tools.calculator_tools import sine_function, exponential_function
from src.bot_config.base_config import BotConfig

calculator_bot_config = BotConfig(
    name="Calculator Chatbot",
    system_instruction=(
        "You are an assistant specializing in calculating sine(x) and exp(x) using the "
        "provided tools. "
    ),
    greeting_message=(
        "Hi! Welcome to the Calculator Chatbot! "
        "Here are some things you can ask me: "
        "- 'sine(x)': Calculate the sine of a number x. "
        "- 'exp(x)': Calculate the exponential of a number x. "
        "Type 'exit' at any time to quit the chat. "
        "Let's get started! "
    ),
    tools=[
        {
            "name": "sine_function",
            "description": ("Calculate sine(x) for a given value of x. "),
            "parameters": {
                "type": "object",
                "properties": {
                    "x": {
                        "type": "number",
                        "description": (
                            "The value of x for which to calculate the sine function."
                        ),
                    },
                },
                "required": ["x"],
                "additionalProperties": False,
            },
            "function": sine_function,
        },
        {
            "name": "exponential_function",
            "description": ("Calculate exp(x) for a given value of x. "),
            "parameters": {
                "type": "object",
                "properties": {
                    "x": {
                        "type": "number",
                        "description": (
                            "The value of x for which to calculate the exponential "
                            "function."
                        ),
                    },
                },
                "required": ["x"],
                "additionalProperties": False,
            },
            "function": exponential_function,
        },
    ],
)
