from src.chatbot.tool_manager import ToolManager
from src.chatbot.chatbot import ChatBot
from src.tools.tool_config import TOOL_CONFIG
from src.helpers.authenticate import get_client
from src.config.weather_bot_config import SYSTEM_INSTRUCTION, GREETING_MESSAGE


def main():
    """
    Main entry point for the chatbot application.
    """
    # Initialize ToolManager with the tool configuration
    tool_manager = ToolManager(tool_config=TOOL_CONFIG)

    # Create the ChatBot with the client and system instruction
    client = get_client()
    chatbot = ChatBot(tool_manager, client, SYSTEM_INSTRUCTION)

    # Display the greeting message
    print(GREETING_MESSAGE)

    # Start the chatbot interaction loop
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye! 👋 Stay safe and enjoy the weather!")
            break
        response = chatbot.process_user_input(user_input)
        print(f"Assistant: {response}")


# This ensures the file can still be run directly
if __name__ == "__main__":
    main()
