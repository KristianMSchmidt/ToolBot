def display_available_bots(available_bots):
    """
    Display a numbered list of available bots.
    """
    print("Available chatbots:")
    for idx, bot in enumerate(available_bots, 1):
        print(f"{idx}. {bot.name}")


def get_bot_selection(available_bots):
    """
    Prompt the user to select a bot and validate input.
    """
    while True:
        try:
            selection = int(input("\nEnter the number of the bot you want to use: "))
            if 1 <= selection <= len(available_bots):
                return available_bots[selection - 1]
            else:
                print(f"Please select a number between 1 and {len(available_bots)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
