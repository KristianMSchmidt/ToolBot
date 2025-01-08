from typing import Any, Dict, Callable, List

from src.logging_config import setup_logging
from src.bot_config.base_tool_config import ToolConfig

logger = setup_logging()


class ToolManager:
    """
    Manages tool definitions and function dispatching.
    """

    def __init__(self, tool_config: List[ToolConfig]):
        """
        Initialize the ToolManager with tools from a configuration.
        """
        self.tools = []
        self.function_map = {}
        self._register_tools(tool_config)

    def _register_tools(self, tool_config: List[ToolConfig]):
        """
        Register tools based on a configuration file.
        """
        for tool in tool_config:
            self.define_tool(
                tool.name, tool.description, tool.parameters, tool.function
            )

    def define_tool(
        self,
        name: str,
        description: str,
        parameters: Dict[str, Any],
        function: Callable,
    ):
        """
        Define a tool and map it to a callable function.
        """
        self.tools.append(
            {
                "type": "function",
                "function": {
                    "name": name,
                    "description": description,
                    "parameters": parameters,
                },
            }
        )
        self.function_map[name] = function

    def call_function(self, function_name: str, arguments: Dict[str, Any]) -> str:
        """
        Call a registered function by name and log the call details.
        """
        try:
            # Log the function call details
            logger.info(
                f"Calling function '{function_name}' with arguments: {arguments}"
            )

            function = self.function_map.get(function_name)
            if not function:
                error_message = f"Error: Function '{function_name}' is not registered."
                logger.error(error_message)
                return error_message

            result = function(**arguments)

            # Log the successful result
            logger.info(f"Function '{function_name}' returned: {result}")
            return result
        except Exception as e:
            # Log the error
            error_message = f"Error calling function '{function_name}': {str(e)}"
            logger.error(error_message)
            return error_message
