from src.tools.weather_tools import get_weather, get_temperature
from unittest.mock import patch

# Mock data for testing
MOCK_WEATHER_RESPONSE = {
    "current": {
        "condition": {"text": "Sunny"},
        "temp_c": 25,
    }
}

MOCK_ERROR_RESPONSE = {"error": "Error fetching weather data: 404"}


# Test get_weather function
def test_get_weather_success():
    with patch("src.tools.weather_tools.fetch_weather_data") as mock_fetch:
        # Mock the fetch_weather_data return value
        mock_fetch.return_value = MOCK_WEATHER_RESPONSE

        result = get_weather("New York", "dummy_api_key")
        assert result == "Weather in New York: Sunny."


def test_get_weather_error():
    with patch("src.tools.weather_tools.fetch_weather_data") as mock_fetch:
        # Mock an error response
        mock_fetch.return_value = MOCK_ERROR_RESPONSE

        result = get_weather("InvalidCity", "dummy_api_key")
        assert result == MOCK_ERROR_RESPONSE["error"]


# Test get_temperature function
def test_get_temperature_success():
    with patch("src.tools.weather_tools.fetch_weather_data") as mock_fetch:
        # Mock the fetch_weather_data return value
        mock_fetch.return_value = MOCK_WEATHER_RESPONSE

        result = get_temperature("New York", "dummy_api_key")
        assert result == "Temperature in New York: 25°C."


def test_get_temperature_error():
    with patch("src.tools.weather_tools.fetch_weather_data") as mock_fetch:
        # Mock an error response
        mock_fetch.return_value = MOCK_ERROR_RESPONSE

        result = get_temperature("InvalidCity", "dummy_api_key")
        assert result == MOCK_ERROR_RESPONSE["error"]
