import os
import sys

sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import requests
from core.configs import settings
from fastapi.testclient import TestClient
from main import app

ENDPOINT = f"{settings.API_URL}/{settings.API_V1_STR}/users"
client = TestClient(app)  # TODO Use the client to make internal requests instead of using the requests library


def test_get_users():
    response = requests.get(f"{ENDPOINT}/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.parametrize("user_id, expected_status", [(1, 200), (999, 404)])
def test_get_user(user_id, expected_status):
    response = requests.get(f"{ENDPOINT}/{user_id}")
    assert response.status_code == expected_status


@pytest.mark.parametrize("user_id, expected_status", [(1, 202), (2, 202)])
def test_update_user(user_id, expected_status):
    payload = {
        "first_name": "João",
        "last_name": "Amgarten",
        "username": "jamgarten",
        "password": "123456",
    }
    response = requests.put(f"{ENDPOINT}/{user_id}", json=payload)
    assert response.status_code == expected_status


@pytest.mark.parametrize("user_id, expected_status", [(1, 204), (2, 204), (999, 404)])
def test_update_deleted_flag(user_id, expected_status):
    response = requests.put(f"{ENDPOINT}/delete/{user_id}")
    assert response.status_code == expected_status
