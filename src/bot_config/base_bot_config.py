from pydantic import BaseModel
from typing import List
from src.bot_config.base_tool_config import ToolConfig


class BotConfig(BaseModel):
    """
    Base class for bot configurations.
    """

    name: str
    system_instruction: str
    greeting_message: str
    tool_config: List[ToolConfig]
