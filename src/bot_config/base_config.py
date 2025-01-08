from pydantic import BaseModel
from typing import List, Dict


class BotConfig(BaseModel):
    """
    Base class for bot configurations.
    """

    name: str
    system_instruction: str
    greeting_message: str
    tools: List[Dict]
