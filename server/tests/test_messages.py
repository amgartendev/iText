"""
Important: Please note that for all tests to pass, you must have users registered in
the database and update the MOCK_USER_UID constants.
"""

import os
import sys
from typing import Type

sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import requests
from core.configs import settings
from fastapi.testclient import TestClient
from main import app

ENDPOINT = f"{settings.API_URL}/{settings.API_V1_STR}/messages"

MOCK_USER_UID_1 = "2fbc5d3b-6ed4-4cc6-9976-c22b355c4316"
MOCK_USER_UID_2 = "d58e8a2e-b60f-429c-a8db-19b30a4a1c31"
MOCK_USER_UID_3 = "c3faf781-1e1a-4e81-9cee-3669ae618e1a"

client = TestClient(app)  # TODO Use the client to make internal requests instead of using the requests library


@pytest.mark.parametrize(
    "sender_uid, recipient_uid, expected_status, succeeded",
    [
        (MOCK_USER_UID_1, MOCK_USER_UID_1, 201, True),
        (MOCK_USER_UID_1, MOCK_USER_UID_2, 201, True),
        (MOCK_USER_UID_2, MOCK_USER_UID_1, 201, True),
        (MOCK_USER_UID_1, MOCK_USER_UID_3, 404, False),
        (MOCK_USER_UID_3, MOCK_USER_UID_3, 404, False),
    ],
)
def test_post_create_message(sender_uid: str, recipient_uid: str, expected_status: int, succeeded: bool) -> None:
    payload = {"content": "Hello, this is a test message from PyTest :)"}
    response = requests.post(f"{ENDPOINT}/{sender_uid}/{recipient_uid}", json=payload)

    assert response.status_code == expected_status
    if succeeded:
        assert "created_at" in response.json()
        assert "content" in response.json()


@pytest.mark.parametrize("user_uid, expected_status, expected_type", [(MOCK_USER_UID_1, 200, list), (MOCK_USER_UID_3, 404, dict)])
def test_get_messages_from_user(user_uid: str, expected_status: int, expected_type: Type) -> None:
    response = requests.get(f"{ENDPOINT}/{user_uid}")
    assert response.status_code == expected_status
    assert isinstance(response.json(), expected_type)


@pytest.mark.parametrize("message_uid, expected_status", [("6668175d-4d42-4637-848c-d48d7cb97e70", 200), (MOCK_USER_UID_3, 404)])
def test_get_message(message_uid: str, expected_status: int) -> None:
    response = requests.get(f"{ENDPOINT}/message/{message_uid}")
    assert response.status_code == expected_status
