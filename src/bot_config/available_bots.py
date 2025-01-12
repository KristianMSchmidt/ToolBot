from src.bot_config.bots.calculator_bot_config import calculator_bot_config
from src.bot_config.bots.weather_bot_config import weather_bot_config
from src.bot_config.bots.chat_gpt_default_config import chat_gpt_default_config

# from src.bot_config.bots.smk_bot_config import smk_bot_config

AVAILABLE_BOTS = [
    chat_gpt_default_config,
    calculator_bot_config,
    weather_bot_config,
    # smk_bot_config,
]
