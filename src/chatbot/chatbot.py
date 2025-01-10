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

    def handle_tool_calls(self, tool_calls: List[Dict[str, Any]]):
        """
        Process tool calls and append results to the chat history.
        """
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            # Call the function and get the result
            result = self.tool_manager.call_function(function_name, arguments)

            # Create the tool message content
            tool_message_content = json.dumps(
                {
                    "arguments": arguments,
                    "result": result,
                }
            )

            # Add the tool message to the chat history
            self.chat_history.append(
                {
                    'role': "tool",
                    'content': tool_message_content,
                    'tool_call_id': tool_call.id,
                }
            )

    def process_user_input(self, user_input: str):
        """
        Process user input and handle tool calls if needed.
        """
        self.chat_history.append({'role': "user", 'content': user_input})

        while True:
            # Call ChatGPT API with messages so far
            completion = self.client.chat.completions.create(
                model="gpt-4o",
                messages=self.chat_history,
                tools=self.tool_manager.tools,
            )
            message = completion.choices[0].message

            # Check if AI wants to use our tools
            if message.tool_calls is not None:
                # Add the tool calls message to the chat history
                self.chat_history.append(message)

                # Handle tool calls
                self.handle_tool_calls(message.tool_calls)

            elif message.content:
                # Append asistants final message to chat history
                self.chat_history.append(
                    {'role': 'assistant', 'content': message.content}
                )
                return message.content
            else:
                return "Error: Assistant response was empty or invalid."
