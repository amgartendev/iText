"""
Important: Please note that for all tests to pass, you must have users registered in
the database and update the UID in the pytest parameters.
"""

import os
import sys

sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import requests
from core.configs import settings
from fastapi.testclient import TestClient
from main import app

ENDPOINT = f"{settings.API_URL}/{settings.API_V1_STR}/messages"
client = TestClient(app)  # TODO Use the client to make internal requests instead of using the requests library


@pytest.mark.parametrize(
    "sender_id, recipient_id, expected_status, succeeded",
    [
        ("2fbc5d3b-6ed4-4cc6-9976-c22b355c4316", "2fbc5d3b-6ed4-4cc6-9976-c22b355c4316", 201, True),
        ("2fbc5d3b-6ed4-4cc6-9976-c22b355c4316", "d58e8a2e-b60f-429c-a8db-19b30a4a1c31", 201, True),
        ("d58e8a2e-b60f-429c-a8db-19b30a4a1c31", "2fbc5d3b-6ed4-4cc6-9976-c22b355c4316", 201, True),
        ("2fbc5d3b-6ed4-4cc6-9976-c22b355c4316", "h1oi2hdj", 404, False),
        ("h1oi2hdj", "h1oi2hdj", 404, False),
    ],
)
def test_post_create_message(sender_id, recipient_id, expected_status, succeeded):
    payload = {"content": "Hello, this is a test message from PyTest :)"}
    response = requests.post(f"{ENDPOINT}/{sender_id}/{recipient_id}", json=payload)

    assert response.status_code == expected_status
    if succeeded:
        assert "created_at" in response.json()
        assert "content" in response.json()


@pytest.mark.parametrize("user_id, expected_status, expected_type", [("2fbc5d3b-6ed4-4cc6-9976-c22b355c4316", 200, list), ("h1oi2hdj", 404, dict)])
def test_get_messages_from_user(user_id, expected_status, expected_type):
    response = requests.get(f"{ENDPOINT}/{user_id}")
    assert response.status_code == expected_status
    assert isinstance(response.json(), expected_type)


@pytest.mark.parametrize("message_uid, expected_status", [("6668175d-4d42-4637-848c-d48d7cb97e70", 200), ("h1oi2hdj", 404)])
def test_get_message(message_uid, expected_status):
    response = requests.get(f"{ENDPOINT}/message/{message_uid}")
    assert response.status_code == expected_status
