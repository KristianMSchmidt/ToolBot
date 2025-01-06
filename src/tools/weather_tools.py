import requests


def get_current_weather(location: str, api_key: str) -> dict:
    """
    Fetches the current weather details for a given location from the Weather API.

    Args:
        location (str): The name of the location (e.g., city or town).
        api_key (str): The API key for the Weather API.

    Returns:
        dict: The current weather details for the location, or an error message
              if the request fails.
    """

    base_url = "http://api.weatherapi.com/v1/current.json"

    try:
        response = requests.get(base_url, params={"key": api_key, "q": location})
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        return data.get("current", {})
    except requests.RequestException as e:
        return {"error": f"Error fetching weather data: {e}"}
