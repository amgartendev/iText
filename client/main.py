import os
import sys

import pygame
import qtawesome
import requests
import utils
from PySide6 import QtCore
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
                               QMainWindow, QWidget)
from ui import Ui_MainWindow


class LoginThread(QThread):
    finished = Signal(int, dict)

    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password

    def run(self):
        payload = {
            "username": self.username,
            "password": self.password
        }
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

class Login(QMainWindow):
    # TODO Separate the Login class from the MainWindow methods
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
        self.ui.button_send_message.clicked.connect(self.send_message)

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

        self.login_thread = LoginThread(username, password)
        self.login_thread.finished.connect(self.on_login_finished)
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


    def send_message(self):
        message = self.ui.input_message.text()
        if not message:
            return

        self.send_message_thread = SendMessageThread(message)
        self.send_message_thread.finished.connect(self.on_message_sent)
        self.send_message_thread.start()

        self.ui.input_message.clear()

    def on_message_sent(self, status_code, response_data):
        if status_code == 201:
            font = QFont()
            font.setPointSize(11)

            message_label = QLabel(self.send_message_thread.message)
            message_label.setWordWrap(True)
            message_label.setFont(font)
            message_label.setStyleSheet("background-color: #007AFF; color: #FFFFFF; padding: 5px; border-radius: 5px;")

            container_widget = QWidget()
            container_widget.setMaximumWidth(300)
            container_widget.setMaximumHeight(100)

            container_layout = QHBoxLayout(container_widget)
            container_layout.addWidget(message_label, alignment=Qt.AlignRight)
            container_layout.setContentsMargins(0, 0, 0, 0)
            container_widget.setLayout(container_layout)

            self.ui.scroll_layout.addWidget(container_widget, alignment=Qt.AlignRight)
            self.ui.scrollArea.verticalScrollBar().setValue(self.ui.scrollArea.verticalScrollBar().maximum())

            pygame.mixer.init()
            pygame.mixer.music.load(os.path.join(utils.AUDIO_FOLDER, "SentMessage.wav"))
            pygame.mixer.music.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.setWindowFlags(window.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
    window.show()
    app.exec()
