from chatbot.tool_manager import ToolManager
from chatbot.chatbot import ChatBot
from tools.tool_config import TOOL_CONFIG  # type: ignore
from helpers.authenticate import get_client

if __name__ == "__main__":
    # Initialize ToolManager with the tool configuration
    tool_manager = ToolManager(tool_config=TOOL_CONFIG)

    # Create the ChatBot with the client and tool manager
    client = get_client()
    chatbot = ChatBot(tool_manager, client)

    print("Weather Chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = chatbot.process_user_input(user_input)
        print(f"Assistant: {response}")
