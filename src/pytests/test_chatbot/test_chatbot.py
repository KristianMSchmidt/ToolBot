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


def test_add_message():
    mock_tool_manager = MagicMock(spec=ToolManager)
    mock_client = MagicMock()

    chatbot = ChatBot(
        tool_manager=mock_tool_manager, client=mock_client, system_instruction=""
    )

    chatbot.add_message("user", "Hello!")
    chatbot.add_message("assistant", "Hi there!", tool_call_id="123")

    assert len(chatbot.chat_history) == 3
    assert chatbot.chat_history[1]["role"] == "user"
    assert chatbot.chat_history[1]["content"] == "Hello!"
    assert chatbot.chat_history[2]["role"] == "assistant"
    assert chatbot.chat_history[2]["content"] == "Hi there!"
    assert chatbot.chat_history[2]["tool_call_id"] == "123"


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


def test_process_user_input_when_tool_calls_in_response():
    # Mock ToolManager
    mock_tool_manager = MagicMock(spec=ToolManager)
    mock_tool_manager.tools = []  # Add a mock attribute for tools
    mock_tool_manager.call_function.return_value = "Sunny in New York"

    # Mock the AI client
    mock_client = MagicMock()
    mock_message = MagicMock()
    mock_message.tool_calls = [
        MagicMock(
            function=MagicMock(
                name="get_weather", arguments=json.dumps({"location": "New York"})
            ),
            id="tool_call_1",
        )
    ]
    mock_message.content = None  # No immediate content; requires tool processing
    mock_client.chat.completions.create.side_effect = [
        MagicMock(choices=[MagicMock(message=mock_message)]),
        MagicMock(
            choices=[
                MagicMock(
                    message=MagicMock(content="Weather fetched: Sunny in New York")
                )
            ]
        ),
    ]

    # Initialize ChatBot with mocks
    chatbot = ChatBot(
        tool_manager=mock_tool_manager, client=mock_client, system_instruction=""
    )

    # Simulate user input
    response = chatbot.process_user_input("What's the weather in New York?")

    # Assert the correct assistant response
    assert response == "Weather fetched: Sunny in New York"

    # Assert the chat history is updated correctly
    assert len(chatbot.chat_history) == 5  # System, user, tool_call, tool, assistant
    assert chatbot.chat_history[1]["role"] == "user"
    assert chatbot.chat_history[1]["content"] == "What's the weather in New York?"
    assert "Sunny in New York" in chatbot.chat_history[3]["content"]
    assert chatbot.chat_history[4]["content"] == "Weather fetched: Sunny in New York"
