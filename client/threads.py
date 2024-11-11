import asyncio
import json

import requests
import utils
import websockets
from PySide6.QtCore import QThread, Signal


async def connect_to_websocket(data: dict, action: str):
    url = "ws://127.0.0.1:8001"
    async with websockets.connect(url) as ws:
        if not data:
            return

        message = {"action": action, "data": data}
        await ws.send(json.dumps(message))
        while True:
            response_data = await ws.recv()


class LoginThread(QThread):
    finished = Signal(int, dict)

    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password

    def run(self):
        payload = {"username": self.username, "password": self.password}
        try:
            request = requests.post(f"{utils.API_URL}/{utils.API_BASE_ENDPOINT}/users/login", json=payload)
            self.finished.emit(request.status_code, request.json())

            # Create and set a new event loop for this thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(connect_to_websocket(request.json(), "login"))
            loop.close()

        except requests.RequestException as error_message:
            self.finished.emit(500, {"error": str(error_message)})


class PopulateContactList(QThread):
    finished = Signal(int, list)

    def __init__(self, user_uid):
        super().__init__()
        self.user_uid = user_uid

    def run(self):
        try:
            request = requests.get(f"{utils.API_URL}/{utils.API_BASE_ENDPOINT}/contacts/{self.user_uid}")
            self.finished.emit(request.status_code, request.json())

            # Create and set a new event loop for this thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(connect_to_websocket(request.json(), "contacts"))
            loop.close()
        except requests.RequestException as error_message:
            self.finished.emit(500, {"error": str(error_message)})


class GetUserInfoThread(QThread):
    finished = Signal(int, dict)

    def __init__(self, user_uid, user_added):
        super().__init__()
        self.user_uid = user_uid
        self.user_added = user_added

    def run(self):
        request = requests.get(f"{utils.API_URL}/{utils.API_BASE_ENDPOINT}/contacts/info/{self.user_uid}/{self.user_added}")
        self.finished.emit(request.status_code, request.json())

        # Create and set a new event loop for this thread
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(connect_to_websocket(request.json(), "users"))
        loop.close()


class SendMessageThread(QThread):
    finished = Signal(int, dict)

    def __init__(self, sender, recipient, message):
        super().__init__()
        self.sender = sender
        self.recipient = recipient
        self.message = message

    def run(self):
        payload = {"content": self.message}
        try:
            request = requests.post(f"{utils.API_URL}/{utils.API_BASE_ENDPOINT}/messages/{self.sender}/{self.recipient}", json=payload)
            self.finished.emit(request.status_code, request.json())

            # Create and set a new event loop for this thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(connect_to_websocket(request.json(), "message"))
            loop.close()
        except requests.RequestException as error_message:
            self.finished.emit(500, {"error": str(error_message)})
