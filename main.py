import sys

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                               QVBoxLayout, QWidget)

from server.api_manager import APIManager
from server.procedures import FlaskServerThread


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.start_server()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Flask Server App")

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        self.api_manager = APIManager(self.server_thread)

        get_user_button = QPushButton("GET USER", self)
        get_user_button.clicked.connect(lambda: self.get_user("jamgarten@example.com"))

        layout.addWidget(get_user_button)
        self.setCentralWidget(central_widget)

    def start_server(self):
        self.server_thread = FlaskServerThread()
        self.server_thread.server_started.connect(self.on_server_started)
        self.server_thread.start()

    def get_user(self, email):
        print(self.api_manager.get_user(email))

    def on_server_started(self):
        print("Flask server started!")


if __name__ == "__main__":
    app_window = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app_window.exec())
