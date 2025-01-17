import json
from unittest.mock import MagicMock
from src.chatbot.chatbot import ChatBot
from src.chatbot.tool_manager import ToolManager


def test_chatbot_initialization():
    mock_tool_manager = MagicMock(spec=ToolManager)
    mock_client = MagicMock()

    chatbot = ChatBot(
        tool_manager=mock_tool_manager, client=mock_client, system_instruction=""
    )

    # Check initial chat history
    assert len(chatbot.chat_history) == 1
    assert chatbot.chat_history[0]["role"] == "system"


def test_handle_tool_calls():
    mock_tool_manager = MagicMock(spec=ToolManager)
    mock_tool_manager.call_function.return_value = "Sunny in New York"

    mock_client = MagicMock()
    chatbot = ChatBot(
        tool_manager=mock_tool_manager, client=mock_client, system_instruction=""
    )

    # Create a mock tool_call object
    mock_tool_call = MagicMock()
    mock_tool_call.function.name = "get_weather"
    mock_tool_call.function.arguments = json.dumps({"location": "New York"})
    mock_tool_call.id = "tool_call_1"

    # Pass the mock tool_call in a list
    chatbot.handle_tool_calls([mock_tool_call])

    # Validate the chat history is updated correctly
    assert len(chatbot.chat_history) == 2
    assert chatbot.chat_history[1]["role"] == "tool"
    assert "Sunny in New York" in chatbot.chat_history[1]["content"]

    # Validate that the tool manager's function was called with the correct arguments
    mock_tool_manager.call_function.assert_called_once_with(
        "get_weather", {"location": "New York"}
    )


def test_process_user_input_when_no_tool_calls_in_response():
    # Mock ToolManager
    mock_tool_manager = MagicMock(spec=ToolManager)
    mock_tool_manager.tools = []  # Add a mock attribute for tools

    # Mock the AI client
    mock_client = MagicMock()
    mock_message = MagicMock()
    mock_message.content = "Hello!"
    mock_message.tool_calls = None
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=mock_message)]
    )

    # Initialize ChatBot with mocks
    chatbot = ChatBot(
        tool_manager=mock_tool_manager, client=mock_client, system_instruction=""
    )

    # Simulate user input
    response = chatbot.process_user_input("Hi!")

    # Assert the correct assistant response
    assert response == "Hello!"

    # Assert the chat history is updated correctly
    assert len(chatbot.chat_history) == 3
    assert chatbot.chat_history[1]["role"] == "user"
    assert chatbot.chat_history[1]["content"] == "Hi!"
    assert chatbot.chat_history[2]["role"] == "assistant"
    assert chatbot.chat_history[2]["content"] == "Hello!"
