import json
from typing import List, Dict, Any
from .tool_manager import ToolManager


class ChatBot:
    """
    Handles chat interactions and manages the assistant's logic.
    """

    def __init__(self, tool_manager: ToolManager, client: Any, system_instruction: str):
        """
        Initialize the ChatBot with a tool manager, client, and system instruction.

        Args:
            tool_manager (ToolManager): The manager for tools the chatbot can use.
            client (Any): The OpenAI API client instance.
            system_instruction (str): The system instruction defining the chatbot's
                behavior.
        """
        self.client = client
        self.tool_manager = tool_manager
        self.chat_history = [
            {
                "role": "system",
                "content": system_instruction,
            }
        ]

    def add_message(self, role: str, content: str, tool_call_id: str = None):
        """
        Add a message to the chat history.
        """
        message = {"role": role, "content": content}
        if tool_call_id:
            message["tool_call_id"] = tool_call_id
        self.chat_history.append(message)

    def handle_tool_calls(self, tool_calls: List[Dict[str, Any]]):
        """
        Process tool calls and append results to the chat history.
        """
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            result = self.tool_manager.call_function(function_name, arguments)
            self.add_message(
                "tool",
                json.dumps({"location": arguments["location"], "result": result}),
                tool_call.id,  # Reference the tool_calls ID
            )

    def process_user_input(self, user_input: str):
        """
        Process user input and handle tool calls if needed.
        """
        self.add_message("user", user_input)

        # Generate model response
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=self.chat_history,
            tools=self.tool_manager.tools,
        )
        message = completion.choices[0].message

        # Check if there are tool calls
        if hasattr(message, "tool_calls") and message.tool_calls:

            # Add the tool calls message to the chat history
            self.chat_history.append(message)

            self.handle_tool_calls(message.tool_calls)

            # Generate another model response using the updated chat history
            completion = self.client.chat.completions.create(
                model="gpt-4o",
                messages=self.chat_history,
            )
            assistant_response = completion.choices[0].message.content
            self.add_message("assistant", assistant_response)
            return assistant_response
        elif message.content:
            self.add_message("assistant", message.content)
            return message.content
        else:
            return "Error: Assistant response was empty or invalid."
