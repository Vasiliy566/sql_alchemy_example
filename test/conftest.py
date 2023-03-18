import pytest
from fastapi.testclient import TestClient

from main import app

lat = 59.938480
lon = 30.312481
temp = 36.6


@pytest.fixture
def test_client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def mock_weather_response(requests_mock):
    requests_mock.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true",
        json={'latitude': 59.93801, 'longitude': 30.32132, 'generationtime_ms': 0.2650022506713867,
              'utc_offset_seconds': 0, 'timezone': 'GMT', 'timezone_abbreviation': 'GMT', 'elevation': 8.0,
              'current_weather': {'temperature': temp, 'windspeed': 14.4, 'winddirection': 149.0, 'weathercode': 0,
                                  'time': '2023-03-17T18:00'}})