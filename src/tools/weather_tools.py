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

        response = requests.get(
            base_url, params={"key": api_key, "q": location}, timeout=10
        )
        response.raise_for_status()
        data = response.json()
        return data.get("current", {})
    except requests.RequestException as e:
        return {"error": f"Error fetching weather data: {e}"}


def get_todays_weather_alerts(api_key, location):
    """
    Fetches weather alerts for today using the WeatherAPI.

    Args:
        api_key (str): Your WeatherAPI key.
        location (str): The location to get alerts for (city, coordinates, or zip code).

    Returns:
        list: A list of simplified alerts for today.
    """
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    params = {"key": api_key, "q": location, "days": 1, "alerts": "yes"}

    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Get current date and alerts
        alerts = data.get("alerts", {}).get("alert", [])

        # Filter and simplify alerts
        todays_alerts = [
            {
                "headline": alert.get("headline"),
                "event": alert.get("event"),
                "severity": alert.get("severity"),
                "areas": alert.get("areas"),
                "effective": alert.get("effective"),
                "expires": alert.get("expires"),
            }
            for alert in alerts
        ]

        return todays_alerts
    except requests.RequestException as e:
        return {"error": f"Error fetching weather alerts: {e}"}
