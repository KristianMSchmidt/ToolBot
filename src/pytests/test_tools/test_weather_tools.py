import requests
from unittest.mock import patch, Mock
from src.tools.weather_tools import (
    get_current_weather,
)


def test_get_current_weather_success():
    """Test successful retrieval of weather data."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "current": {
            "temp_c": 22.5,
            "condition": {"text": "Sunny"},
        }
    }

    with patch("requests.get", return_value=mock_response):
        api_key = "test_api_key"
        location = "Copenhagen"
        result = get_current_weather(location, api_key)

    assert result == {
        "temp_c": 22.5,
        "condition": {"text": "Sunny"},
    }


def test_get_current_weather_failure_http_error():
    """Test behavior when an HTTP error occurs."""
    with patch("requests.get", side_effect=requests.HTTPError("HTTP Error")):
        api_key = "test_api_key"
        location = "Copenhagen"
        result = get_current_weather(location, api_key)

    assert "error" in result
    assert "HTTP Error" in result["error"]


def test_get_current_weather_failure_connection_error():
    """Test behavior when a connection error occurs."""
    with patch(
        "requests.get", side_effect=requests.ConnectionError("Connection Error")
    ):
        api_key = "test_api_key"
        location = "Copenhagen"
        result = get_current_weather(location, api_key)

    assert "error" in result
    assert "Connection Error" in result["error"]


def test_get_current_weather_failure_timeout():
    """Test behavior when a timeout occurs."""
    with patch("requests.get", side_effect=requests.Timeout("Timeout Error")):
        api_key = "test_api_key"
        location = "Copenhagen"
        result = get_current_weather(location, api_key)

    assert "error" in result
    assert "Timeout Error" in result["error"]
