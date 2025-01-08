import os


def list_available_bots(config_path: str = "src/config/bot_config") -> list[str]:
    """
    Lists available bot configurations by inspecting the config directory.
    """
    bot_files = [
        f.replace("_config.py", "")
        for f in os.listdir(config_path)
        if f.endswith("_config.py") and not f.startswith("__")
    ]
    return sorted(bot_files)
