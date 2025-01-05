import requests


def fetch_weather_data(location: str, api_key: str) -> dict:
    """
    Fetches weather data from the Weather API for a given location.

    Args:
        location (str): The name of the location (e.g., city or town).
        api_key (str): The API key for the Weather API.

    Returns:
        dict: The JSON response from the API, or an empty dictionary if the request fails.
    """
    base_url = "http://api.weatherapi.com/v1/current.json"
    response = requests.get(base_url, params={"key": api_key, "q": location})

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Error fetching weather data: {response.status_code}"}


def get_weather(location: str, api_key: str) -> str:
    """
    Fetches the current weather condition for a given location.

    Args:
        location (str): The name of the location (e.g., city or town).
        api_key (str): The API key for the Weather API.

    Returns:
        str: A string describing the current weather in the location, or an error message.
    """
    data = fetch_weather_data(location, api_key)

    if "error" in data:
        return data["error"]
    else:
        condition = data["current"]["condition"]["text"]
        return f"Weather in {location}: {condition}."


def get_temperature(location: str, api_key: str) -> str:
    """
    Fetches the current temperature for a given location.

    Args:
        location (str): The name of the location (e.g., city or town).
        api_key (str): The API key for the Weather API.

    Returns:
        str: A string describing the current temperature in the location, or an error message.
    """
    data = fetch_weather_data(location, api_key)

    if "error" in data:
        return data["error"]
    else:
        temperature = data["current"]["temp_c"]
        return f"Temperature in {location}: {temperature}°C."
