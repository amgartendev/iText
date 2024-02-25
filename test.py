from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import QThread, Signal
from server.api_manager import APIManager
from server.procedures import FlaskServerThread
import sys

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
        get_user_button.clicked.connect(self.api_manager.get_user)
        self.api_manager.api_response_received.connect(self.handle_api_response)

        layout.addWidget(get_user_button)
        self.setCentralWidget(central_widget)

    def start_server(self):
        self.server_thread = FlaskServerThread()
        self.server_thread.server_started.connect(self.on_server_started)
        self.server_thread.start()

    def on_server_started(self):
        print("Flask server started!")

    def handle_api_response(self, response):
        print(response)

if __name__ == "__main__":
    app_window = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app_window.exec_())
