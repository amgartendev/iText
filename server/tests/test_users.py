"""
Important: Please note that for all tests to pass, you must have users registered in
the database and update the MOCK_USER_UID and MOCK_USERNAME constants.
"""

import os
import sys

sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import requests
from core.configs import settings
from fastapi.testclient import TestClient
from main import app

ENDPOINT = f"{settings.API_URL}/{settings.API_V1_STR}/users"

MOCK_USER_UID_1 = "2fbc5d3b-6ed4-4cc6-9976-c22b355c4316"
MOCK_USER_UID_2 = "d58e8a2e-b60f-429c-a8db-19b30a4a1c31"
MOCK_USERNAME_1 = "jamgarten"
MOCK_USERNAME_2 = "h1oi2hdj"

client = TestClient(app)  # TODO Use the client to make internal requests instead of using the requests library


def test_get_users() -> None:
    response = requests.get(f"{ENDPOINT}/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.parametrize("user_uid, expected_status", [(MOCK_USER_UID_1, 200), (MOCK_USERNAME_2, 404)])
def test_get_user(user_uid: str, expected_status: int) -> None:
    response = requests.get(f"{ENDPOINT}/{user_uid}")
    assert response.status_code == expected_status


@pytest.mark.parametrize("user_uid, expected_status", [(MOCK_USER_UID_1, 202), (MOCK_USER_UID_2, 406)])
def test_update_user(user_uid: str, expected_status: int) -> None:
    payload = {
        "first_name": "João",
        "last_name": "Amgarten",
        "username": MOCK_USERNAME_1,
        "password": "123456",
    }
    response = requests.put(f"{ENDPOINT}/{user_uid}", json=payload)
    assert response.status_code == expected_status


@pytest.mark.parametrize("user_uid, expected_status", [(MOCK_USER_UID_1, 204), (MOCK_USER_UID_2, 204), (MOCK_USERNAME_2, 404)])
def test_update_deleted_flag(user_uid: str, expected_status: int) -> None:
    response = requests.put(f"{ENDPOINT}/delete/{user_uid}")
    assert response.status_code == expected_status


@pytest.mark.parametrize("username, password, expected_status", [(MOCK_USERNAME_1, "123456", 200), (MOCK_USERNAME_1, "123", 401), (MOCK_USERNAME_2, "123456", 401)])
def test_login(username: str, password: str, expected_status: int):
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(f"{ENDPOINT}/login/", json=payload)
    assert response.status_code == expected_status
