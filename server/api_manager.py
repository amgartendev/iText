import re

from PySide6.QtCore import QObject, Signal

from server.error_codes import error_codes_list
from server.procedures import FlaskServerThread


class APIManager(QObject):
    api_response_received = Signal(str)

    def __init__(self, server_thread: FlaskServerThread):
        super().__init__()
        self.server_thread = server_thread

    def get_user(self, email):
        if not email:
            return

        try:
            response = self.server_thread.get_user(email)
            return response, 200
        except Exception as error_code:
            error_code_pattern = re.compile(r"^(\w+)", re.MULTILINE)
            match = error_code_pattern.search(str(error_code))
            error_code = match.group(1)
            return {
                "error_code": error_code,
                "error_message": error_codes_list[error_code],
            }, 500
