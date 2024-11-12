import os
import sys

import pygame
import utils
from login_window import Login
from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor, QFont, QPixmap
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
                               QPushButton, QVBoxLayout, QWidget)
from threads import GetUserInfoThread, PopulateContactList, SendMessageThread
from ui import Ui_MainWindow


class MainWindow(QMainWindow):
    pygame.mixer.init()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.profile = None
        self.current_chat = None

        self.ui.button_send_message.clicked.connect(self.send_message)

    def setup_ui(self):
        self.ui.label_profile_name.setText(f"{self.profile['first_name']} {self.profile['last_name']}")
        self.ui.label_username.setText(f"@{self.profile['username']}")
        self.ui.image_profile.setPixmap(QPixmap(os.path.join(utils.PROFILE_IMAGES_FOLDER, "default.png")))
        self.populate_contact_list(self.profile["user_uid"])

    def populate_contact_list(self, user_uid):
        self.populate_contact_list_thread = PopulateContactList(user_uid)
        self.populate_contact_list_thread.finished.connect(self.populate)
        self.populate_contact_list_thread.start()
    
    def populate(self, status_code, response_data):
        if status_code == 200:
            font = QFont()
            font.setPointSize(11)

            main_container = QWidget()
            main_layout = QVBoxLayout(main_container)

            for contact in response_data:
                user_added = contact["user_added"]
                contact_name = contact["contact_name"]

                button_conversation = QPushButton(f"{contact_name}")
                button_conversation.setProperty("user_uid", user_added)
                button_conversation.setMinimumHeight(70)
                button_conversation.setMaximumHeight(70)
                button_conversation.setFont(font)
                button_conversation.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                button_conversation.setStyleSheet("QPushButton {border: none; border-bottom: 1.2px solid #CCCFCD;} QPushButton:hover {background-color: #CCCCCC;}")

                button_conversation.clicked.connect(lambda _, user_added=user_added: self.conversation_button(user_added))

                container = QWidget()

                container_layout = QHBoxLayout(container)
                container_layout.addWidget(button_conversation)
                container_layout.setContentsMargins(0, 0, 0, 0)
                container.setLayout(container_layout)

                main_layout.addWidget(container)

            main_container.setLayout(main_layout)
            self.ui.scrollArea.setWidget(main_container)

    def conversation_button(self, user_added):
        self.populate_contact_list_thread = GetUserInfoThread(self.profile["user_uid"], user_added)
        self.populate_contact_list_thread.finished.connect(self.setup_conversation)
        self.populate_contact_list_thread.start()
    
    def setup_conversation(self, status_code, response_data):
        self.current_chat = response_data["user_added"]
        if status_code == 200:
            contact_name = response_data["contact_name"]
            self.ui.label_contact_name.setText(contact_name)

    def send_message(self):
        sender = self.profile["user_uid"]
        recipient = self.current_chat
        message = self.ui.input_message.text()
        if not message:
            return
        self.send_message_thread = SendMessageThread(sender, recipient, message)
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
