import sys

import qtawesome
import requests
import utils
from ui import Ui_MainWindow
from PySide6 import QtCore
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow
from PySide6.QtGui import QPixmap
import os


class LoginThread(QThread):
    def __init__(self, username, password, on_finished):
        super().__init__()
        self.username = username
        self.password = password
        self.on_finished = on_finished

    def run(self):
        payload = {
            "username": self.username,
            "password": self.password
        }
        try:
            request = requests.post(f"{utils.API_URL}/{utils.API_BASE_ENDPOINT}/users/login", json=payload)
            self.on_finished(request.status_code, request.json())
        except requests.RequestException as error_message:
            self.on_finished(500, {"error": str(error_message)})


class Login(QMainWindow):
    login_finished = Signal(int, dict)

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("iText")
        self.profile = None
        self.client_uid = None
        self.is_password_revealed = False
        self.running_thread = False

        self.ui.button_reveal_password.clicked.connect(self.show_password)
        self.ui.button_login.clicked.connect(self.login)

    def show_password(self):
        if not self.is_password_revealed:
            self.ui.input_password.setEchoMode(QLineEdit.EchoMode.Normal)
            self.ui.button_reveal_password.setIcon(qtawesome.icon('fa5.eye-slash', color="#007AFF"))
            self.is_password_revealed = True
        else:
            self.ui.input_password.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.button_reveal_password.setIcon(qtawesome.icon('fa5.eye', color="#007AFF"))
            self.is_password_revealed = False

    def login(self):
        if self.running_thread:
            return
        username: str = self.ui.input_username.text()
        password: str = self.ui.input_password.text()

        self.login_thread = LoginThread(username, password, self.on_login_finished)
        self.login_thread.start()
        self.running_thread = True

    def on_login_finished(self, status_code, response_data):
        self.running_thread = False
        if status_code == 200:
            self.profile = response_data
            self.client_uid = self.profile["user_uid"]
            self.set_ui()
            self.ui.stackedWidget.setCurrentIndex(2)
            print("User logged in -", self.client_uid)  # TODO Add log

        if status_code == 401:
            self.ui.label_error_message.setText(response_data["detail"])
            self.ui.label_error_message.setHidden(False)
            print("User tried to login")  # TODO Add log

    def set_ui(self):
        # Add profile information
        full_name = f"{self.profile["first_name"]} {self.profile["last_name"]}"
        self.ui.label_profile_name.setText(full_name)
        self.ui.label_username.setText(f"@{self.profile["username"]}")
        self.ui.image_profile.setPixmap(QPixmap(os.path.join(utils.PROFILE_IMAGES_FOLDER, "image.png")))

        # Populate contact list


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.setWindowFlags(window.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
    window.show()
    app.exec()
