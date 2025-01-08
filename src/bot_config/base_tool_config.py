from pydantic import BaseModel
from typing import Any


class ToolConfig(BaseModel):
    """
    Base class for tool configurations.
    """

    name: str
    description: str
    parameters: dict
    function: Any  # This is a placeholder for the actual function type
