import asyncio
import json

import requests
import utils
import websockets
from PySide6.QtCore import QThread, Signal


async def connect_to_websocket(data: dict, action: str):
    url = "ws://127.0.0.1:8001"

    async with websockets.connect(url) as ws:
        data.update({"action": action})
        await ws.send(json.dumps(data))
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


class SendMessageThread(QThread):
    finished = Signal(int, dict)

    def __init__(self, message):
        super().__init__()
        self.message = message

    def run(self):
        payload = {"content": self.message}
        try:
            request = requests.post(f"{utils.API_URL}/{utils.API_BASE_ENDPOINT}/messages/1/2", json=payload)
            self.finished.emit(request.status_code, request.json())

            # Create and set a new event loop for this thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(connect_to_websocket(request.json(), "message"))
            loop.close()
        except requests.RequestException as error_message:
            self.finished.emit(500, {"error": str(error_message)})
