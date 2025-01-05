import logging
import os


def setup_logging():
    # Ensure the logs directory exists
    log_dir = os.path.join(os.path.dirname(__file__), "logs")
    os.makedirs(log_dir, exist_ok=True)

    # Configure logging
    log_file = os.path.join(log_dir, "tool_calls.log")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            # Uncomment to enable console logging
            # logging.StreamHandler(),
            logging.FileHandler(log_file),
        ],
    )
    return logging.getLogger(__name__)
