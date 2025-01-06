from src.chatbot.tool_manager import ToolManager
from src.chatbot.chatbot import ChatBot
from src.tools.tool_config import TOOL_CONFIG  # type: ignore
from src.helpers.authenticate import get_client


def main():
    """
    Main entry point for the chatbot application.
    Initializes the tool manager and chatbot, displays a welcome message,
    and starts the interaction loop with the user.
    """
    # Initialize ToolManager with the tool configuration
    tool_manager = ToolManager(tool_config=TOOL_CONFIG)

    # Create the ChatBot with the client and tool manager
    client = get_client()
    chatbot = ChatBot(tool_manager, client)

    # Display a clear and engaging welcome message
    print("🌦️ Hi! Welcome to the Weather Chatbot! 🌟")
    print("I'm here to help you with all your weather-related questions.")
    print("\nHere are some things you can ask me:")
    print("- 'What is the weather like in Copenhagen?'")
    print("- 'What should I wear in Athens today?'")
    print("- 'What tires should I use in Helsinki today?'")
    print("- 'What is the temperature in China's 5 biggest cities today?'")
    print("\n💡 Type 'exit' at any time to quit the chat.")
    print("Let's get started! 🌈")

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
