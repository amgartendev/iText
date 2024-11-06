import requests
import utils
from PySide6.QtCore import QThread, Signal


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
            request = requests.post(f"{utils.API_URL}/{utils.API_BASE_ENDPOINT}/messages/1/1", json=payload)
            self.finished.emit(request.status_code, request.json())
        except requests.RequestException as error_message:
            self.finished.emit(500, {"error": str(error_message)})
