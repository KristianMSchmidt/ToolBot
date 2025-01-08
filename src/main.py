import importlib
from src.config.utils import list_available_bots
from src.interface.cli import display_available_bots, get_bot_selection
from src.chatbot.tool_manager import ToolManager
from src.chatbot.chatbot import ChatBot
from src.helpers.authenticate import get_client


def main():
    # Discover available bots
    available_bots = list_available_bots()
    if not available_bots:
        print("No bot configurations found. Exiting.")
        return

    # Interact with the user to select a bot
    display_available_bots(available_bots)
    bot_name = get_bot_selection(available_bots)

    # Load the selected bot's configuration
    try:
        bot_config = importlib.import_module(f"src.config.bot_config.{bot_name}_config")
    except ModuleNotFoundError:
        print(f"Error: Bot configuration '{bot_name}_config' not found.")
        return

    # Initialize components
    tool_manager = ToolManager(tool_config=bot_config.TOOLS)
    client = get_client()
    chatbot = ChatBot(tool_manager, client, bot_config.SYSTEM_INSTRUCTION)

    # Display a welcome message and start the chatbot
    print(f"\n{bot_config.GREETING_MESSAGE}")
    run_chatbot(chatbot)


def run_chatbot(chatbot):
    """
    Run the chatbot interaction loop.
    """
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye! 👋")
            break
        response = chatbot.process_user_input(user_input)
        print(f"Assistant: {response}")


if __name__ == "__main__":
    main()
