"""
Important: Please note that for all tests to pass, you must have users registered in
the database and update the MOCK_USER_UID constants.
"""

import os
import sys

sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import Type

import pytest
import requests
from core.configs import settings
from fastapi.testclient import TestClient
from main import app

ENDPOINT = f"{settings.API_URL}/{settings.API_V1_STR}/contacts"

MOCK_USER_UID_1 = "2fbc5d3b-6ed4-4cc6-9976-c22b355c4316"
MOCK_USER_UID_2 = "d58e8a2e-b60f-429c-a8db-19b30a4a1c31"
MOCK_USER_UID_3 = "c3faf781-1e1a-4e81-9cee-3669ae618e1a"

client = TestClient(app)  # TODO Use the client to make internal requests instead of using the requests library


@pytest.mark.parametrize("user_uid, expected_status, expected_type", [(MOCK_USER_UID_1, 200, list), (MOCK_USER_UID_3, 404, dict)])
def test_get_contacts(user_uid: str, expected_status: int, expected_type: Type) -> None:
    response = requests.get(f"{ENDPOINT}/{user_uid}")
    assert response.status_code == expected_status
    assert isinstance(response.json(), expected_type)


@pytest.mark.parametrize(
    "user_uid, contact_uid, contact_name, expected_status", [
        (MOCK_USER_UID_1, MOCK_USER_UID_2, "PyTest Contact", 201),
        (MOCK_USER_UID_1, MOCK_USER_UID_2, "PyTest Contact", 406),
        (MOCK_USER_UID_3, MOCK_USER_UID_2, "PyTest Contact", 404),
        (MOCK_USER_UID_2, MOCK_USER_UID_3, "PyTest Contact", 404),
    ],
)
def test_post_create_contact(user_uid: str, contact_uid: str, contact_name: str, expected_status: int) -> None:
    payload = {
        "user_uid": user_uid,
        "user_added": contact_uid,
        "contact_name": contact_name
    }
    response = requests.post(f"{ENDPOINT}/", json=payload)
    assert response.status_code == expected_status


@pytest.mark.parametrize("user_uid, contact_uid, expected_status", [(MOCK_USER_UID_1, MOCK_USER_UID_2, 200), (MOCK_USER_UID_1, MOCK_USER_UID_3, 404)])
def test_get_contact_info(user_uid: str, contact_uid: str, expected_status: int):
    response = requests.get(f"{ENDPOINT}/info/{user_uid}/{contact_uid}")
    assert response.status_code == expected_status
