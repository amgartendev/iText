from PySide6.QtCore import QObject, Signal
from server.procedures import FlaskServerThread

class APIManager(QObject):
    api_response_received = Signal(str)

    def __init__(self, server_thread: FlaskServerThread):
        super().__init__()
        self.server_thread = server_thread

    def get_user(self):
        response = self.server_thread.get_user()
        self.api_response_received.emit(response)

        print(response)
