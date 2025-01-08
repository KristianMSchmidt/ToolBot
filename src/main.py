from src.interface.cli import display_available_bots, get_bot_selection
from src.chatbot.tool_manager import ToolManager
from src.chatbot.chatbot import ChatBot
from src.helpers.authenticate import get_client
from src.bot_config.available_bots import AVAILABLE_BOTS
from src.bot_config.utils import load_bot_config


def main():

    if not AVAILABLE_BOTS:
        print("No bot configurations found. Exiting.")
        return

    # Interact with the user to select a bot
    display_available_bots(AVAILABLE_BOTS)
    bot_name = get_bot_selection(AVAILABLE_BOTS)

    # Load the selected bot configuration
    bot_config = load_bot_config(bot_name)

    # Initialize components
    tool_manager = ToolManager(tool_config=bot_config.tools)
    client = get_client()
    chatbot = ChatBot(tool_manager, client, bot_config.system_instruction)

    # Display a welcome message and start the chatbot
    print(f"\n{bot_config.greeting_message}")
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
