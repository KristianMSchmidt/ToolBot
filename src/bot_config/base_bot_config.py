from pydantic import BaseModel
from typing import List
from src.bot_config.base_tool_config import ToolConfig


class BotConfig(BaseModel):
    """
    Base class for bot configurations.
    """

    name: str
    system_instruction: str = "You are a helpful assistant"
    greeting_message: str = "How can I help you?"
    tool_config: List[ToolConfig] = []
