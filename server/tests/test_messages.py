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
        (1, 1, 201, True),
        (1, 2, 201, True),
        (2, 1, 201, True),
        (999, 1, 404, False),
        (1, 999, 404, False),
        (999, 999, 404, False),
    ],
)
def test_post_create_message(sender_id, recipient_id, expected_status, succeeded):
    payload = {"content": "Hello, this is a test message from PyTest :)"}
    response = requests.post(f"{ENDPOINT}/{sender_id}/{recipient_id}", json=payload)

    assert response.status_code == expected_status
    if succeeded:
        assert "created_at" in response.json()
        assert "content" in response.json()


@pytest.mark.parametrize("user_id, expected_status, expected_type", [(1, 200, list), (99999, 404, dict)])
def test_get_messages_from_user(user_id, expected_status, expected_type):
    response = requests.get(f"{ENDPOINT}/{user_id}")
    assert response.status_code == expected_status
    assert isinstance(response.json(), expected_type)


@pytest.mark.parametrize("message_uid, expected_status", [("jdsakjhdasjk", 404)])
def test_get_message(message_uid, expected_status):
    response = requests.get(f"{ENDPOINT}/message/{message_uid}")
    assert response.status_code == expected_status
