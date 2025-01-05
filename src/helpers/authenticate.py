"""
Helper function to authenticate with the OpenAI API.
"""

from openai import OpenAI
import os
import dotenv


def get_client():
    """
    Helper function to authenticate with the OpenAI API.
    """
    # Load the environment variables from the .env file
    dotenv.load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    assert api_key is not None, "Please set the OPENAI_API_KEY environment variable."

    client = OpenAI(api_key=api_key)
    return client
