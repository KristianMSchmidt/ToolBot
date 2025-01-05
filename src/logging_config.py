# logging_config.py
import logging


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            # Uncomment the following line to enable logging to the console
            # logging.StreamHandler(),
            logging.FileHandler("tool_calls.log"),
        ],
    )
    return logging.getLogger(__name__)
