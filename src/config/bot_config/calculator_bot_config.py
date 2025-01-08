from src.tools.calculator_tools import sine_function, exponential_function

# System instruction for the weather chatbot
SYSTEM_INSTRUCTION = (
    "You are an assistant specializing in calculating sine(x) and exp(x) using the provided tools. "
    "You can also calculate composite functions using these tools."
    "When given a question such as sin(exp(3)) don't reply before you have calculated the result the final result (use first 1 tool, then the other tool)."
)

# Greeting message displayed to the user
GREETING_MESSAGE = """
Hi! Welcome to the Calculator Chatbot!
Here are some things you can ask me:
- 'sine(x)': Calculate the sine of a number x.
- 'exp(x)': Calculate the exponential of a number x.
- 'composite': Calculate the composite function of sine(exp(x)).

Type 'exit' at any time to quit the chat.
Let's get started!
"""

TOOLS = [
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
                        "The value of x for which to calculate the exponential function."
                    ),
                },
            },
            "required": ["x"],
            "additionalProperties": False,
        },
        "function": exponential_function,
    },
]
