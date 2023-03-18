import pytest
import requests
from app.services.weather_getter import get_my_temp, get_close
from main import app

from fastapi import FastAPI
from fastapi.testclient import TestClient

from test.conftest import lat, lon


def test_my_temperature():
    res = get_close(lat, lon)
    assert res == "На улице жарко, надеть футболку"


def test_read_main(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {'Hello': 'World1'}


def test_get_close(test_client):
    response = test_client.get("/api/get_close", params={"lat": lat, "lon": lon})

    assert response.status_code == 200
    assert response.json() == 'На улице жарко, надеть футболку'
