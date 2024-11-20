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

ENDPOINT = f"{settings.API_URL}/{settings.API_V1_STR}/contacts"
client = TestClient(app)  # TODO Use the client to make internal requests instead of using the requests library


@pytest.mark.parametrize("user_uid, expected_status, expected_type", [("2fbc5d3b-6ed4-4cc6-9976-c22b355c4316", 200, list), ("h1oi2hdj", 404, dict)])
def test_get_contacts(user_uid, expected_status, expected_type):
    response = requests.get(f"{ENDPOINT}/{user_uid}")
    assert response.status_code == expected_status
    assert isinstance(response.json(), expected_type)


@pytest.mark.parametrize("user_uid, contact_uid, contact_name, expected_status", [("2fbc5d3b-6ed4-4cc6-9976-c22b355c4316", "d58e8a2e-b60f-429c-a8db-19b30a4a1c31", "PyTest Contact", 201), ("2fbc5d3b-6ed4-4cc6-9976-c22b355c4316", "d58e8a2e-b60f-429c-a8db-19b30a4a1c31", "PyTest Contact", 406), ("h1oi2hdj", "d58e8a2e-b60f-429c-a8db-19b30a4a1c31", "PyTest Contact", 404), ("d58e8a2e-b60f-429c-a8db-19b30a4a1c31", "h1oi2hdj", "PyTest Contact", 404)])
def test_post_create_contact(user_uid, contact_uid, contact_name, expected_status):
    payload = {
        "user_uid": user_uid,
        "user_added": contact_uid,
        "contact_name": contact_name
    }
    response = requests.post(f"{ENDPOINT}/", json=payload)
    assert response.status_code == expected_status


@pytest.mark.parametrize("user_uid, contact_uid, expected_status", [("2fbc5d3b-6ed4-4cc6-9976-c22b355c4316", "d58e8a2e-b60f-429c-a8db-19b30a4a1c31", 200), ("2fbc5d3b-6ed4-4cc6-9976-c22b355c4316", "h1oi2hdj", 404)])
def test_get_contact_info(user_uid, contact_uid, expected_status):
    response = requests.get(f"{ENDPOINT}/info/{user_uid}/{contact_uid}")
    assert response.status_code == expected_status
