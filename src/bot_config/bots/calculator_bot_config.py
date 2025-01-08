from src.tools.calculator_tools import sine_function, exponential_function
from src.bot_config.base_bot_config import BotConfig
from src.bot_config.base_tool_config import ToolConfig

calculator_bot_config = BotConfig(
    name="Calculator Chatbot",
    system_instruction=(
        "You are an assistant specializing in calculating sine(x) and exp(x) using the "
        "provided tools. "
    ),
    greeting_message="""
    Hi! Welcome to the Calculator Chatbot!
    Here are some things you can ask me:
    - 'sine(x)': Calculate the sine of a number x.
    - 'exp(x)': Calculate the exponential of a number x.
    Type 'exit' at any time to quit the chat.
    Let's get started! "
    """,
    tool_config=[
        ToolConfig(
            name="sine_function",
            description="Calculate sine(x) for a given value of x.",
            parameters={
                "type": "object",
                "properties": {
                    "x": {
                        "type": "number",
                        "description": "The value of x for which to calculate "
                        "the sine function.",
                    }
                },
                "required": ["x"],
                "additionalProperties": False,
            },
            function=sine_function,
        ),
        ToolConfig(
            name="exponential_function",
            description="Calculate exp(x) for a given value of x.",
            parameters={
                "type": "object",
                "properties": {
                    "x": {
                        "type": "number",
                        "description": "The value of x for which to calculate the "
                        "exponential function.",
                    }
                },
                "required": ["x"],
                "additionalProperties": False,
            },
            function=exponential_function,
        ),
    ],
)
