import importlib
from src.bot_config.base_bot_config import BotConfig


def load_bot_config(bot_name: str) -> BotConfig:
    """
    Dynamically loads a bot configuration.
    """
    try:
        module = importlib.import_module(f"src.bot_config.bots.{bot_name}_config")
        return getattr(module, f"{bot_name}_config")
    except (ModuleNotFoundError, AttributeError) as e:
        raise RuntimeError(f"Error loading bot configuration for '{bot_name}': {e}")
