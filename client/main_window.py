import os
import sys

import pygame
import utils
from login_window import Login
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
                               QWidget)
from threads import SendMessageThread
from ui import Ui_MainWindow


class MainWindow(QMainWindow):
    pygame.mixer.init()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.profile = None

        self.ui.button_send_message.clicked.connect(self.send_message)

    def setup_ui(self):
        self.ui.label_profile_name.setText(f"{self.profile['first_name']} {self.profile['last_name']}")
        self.ui.label_username.setText(f"@{self.profile['username']}")
        self.ui.image_profile.setPixmap(QPixmap(os.path.join(utils.PROFILE_IMAGES_FOLDER, "image.png")))

    def send_message(self):
        message = self.ui.input_message.text()
        if not message:
            return
        self.send_message_thread = SendMessageThread(message)
        self.send_message_thread.finished.connect(self.display_message)
        self.send_message_thread.start()

        self.ui.input_message.clear()

    def display_message(self, status_code, response_data):
        if status_code == 201:
            message = response_data["content"]
            sender = response_data["sender"] 
            alignment = Qt.AlignRight if self.profile["user_uid"] == sender else Qt.AlignLeft

            font = QFont()
            font.setPointSize(11)

            message_label = QLabel(message)
            message_label.setWordWrap(True)
            if self.profile["user_uid"] == sender:
                message_label.setStyleSheet("background-color: #007AFF; color: #FFFFFF; padding: 5px; border-radius: 5px;")
            else:
                message_label.setStyleSheet("background-color: red; color: #FFFFFF; padding: 5px; border-radius: 5px;")
            container = QWidget()
            container.setMaximumWidth(300)
            container.setMaximumHeight(100)

            container_layout = QHBoxLayout(container)
            container_layout.addWidget(message_label, alignment=alignment)
            container_layout.setContentsMargins(0, 0, 0, 0)
            container.setLayout(container_layout)

            self.ui.scroll_layout.addWidget(container, alignment=alignment)
            self.ui.scrollArea.verticalScrollBar().setValue(self.ui.scrollArea.verticalScrollBar().maximum())

            pygame.mixer.music.load(os.path.join(utils.AUDIO_FOLDER, "SentMessage.wav"))
            pygame.mixer.music.play()

    def handle_login_success(self, status_code, profile_data):
        if status_code == 200:
            login_window.close()
            self.profile = profile_data
            self.setup_ui()
            self.ui.stackedWidget.setCurrentIndex(2)
            self.show()
        else:
            print("Login failed:", profile_data.get("detail", "Unknown error"))  # TODO Add log


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = Login()
    main_window = MainWindow()

    # Connect login success to the handler function
    login_window.login_finished.connect(main_window.handle_login_success)

    # Show the login window
    login_window.show()
    app.exec()
