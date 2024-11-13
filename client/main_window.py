import os
import sys

import pygame
import qtawesome
import utils
from login_window import Login
from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor, QFont, QPixmap
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
                               QLineEdit, QMainWindow, QPushButton,
                               QVBoxLayout, QWidget)
from threads import (AddContactThread, GetConversationThread,
                     GetUIDByUsernameThread, GetUserInfoThread,
                     PopulateContactList, SendMessageThread)
from ui import Ui_MainWindow


class MainWindow(QMainWindow):
    pygame.mixer.init()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("iText")
        self.profile = None
        self.current_chat = None

        self.ui.button_send_message.clicked.connect(self.send_message)
        self.ui.button_add_contact.clicked.connect(self.add_contact_dialog)

    def setup_ui(self):
        self.ui.button_settings.setIcon(qtawesome.icon("fa5s.cog"))
        self.ui.button_logout.setIcon(qtawesome.icon("fa5s.sign-out-alt"))

        first_name = self.profile["first_name"]
        last_name = self.profile["last_name"]
        username = self.profile["username"]
        profile_picture = self.profile["profile_picture"]

        image_found = os.path.isfile(os.path.join(utils.PROFILE_IMAGES_FOLDER, profile_picture))
        if not image_found:
            profile_picture = "default.png"

        self.ui.label_profile_name.setText(f"{first_name} {last_name}")
        self.ui.label_username.setText(f"@{username}")
        self.ui.image_profile.setPixmap(QPixmap(os.path.join(utils.PROFILE_IMAGES_FOLDER, profile_picture)))
        self.populate_contact_list(self.profile["user_uid"])

    def add_contact_dialog(self):
        dialog = QDialog()
        dialog.setFixedSize(520, 80)
        dialog.setWindowTitle("iText - Add new contact")
        dialog.setModal(True)

        font = QFont()
        font.setPointSize(10)

        Vlayout = QVBoxLayout()
        Hlayout = QHBoxLayout()

        self.line_edit_contact_username = QLineEdit()
        self.line_edit_contact_username.setFont(font)
        self.line_edit_contact_username.setPlaceholderText("Add contacts by their username")

        self.line_edit_contact_name = QLineEdit()
        self.line_edit_contact_name.setFont(font)
        self.line_edit_contact_name.setPlaceholderText("Contact name")

        self.button_add = QPushButton("Add Contact")
        self.button_add.clicked.connect(self.add_contact_thread)
        self.button_add.setFont(font)

        Hlayout.addWidget(self.line_edit_contact_username)
        Hlayout.addWidget(self.line_edit_contact_name)
        Hlayout.addWidget(self.button_add)

        self.feedback_message = QLabel("Feedback Message")
        self.feedback_message.setFont(font)
        self.feedback_message.setAlignment(Qt.AlignCenter)
        self.feedback_message.setWordWrap(True)
        self.feedback_message.setHidden(True)

        Vlayout.addLayout(Hlayout)
        Vlayout.addWidget(self.feedback_message)

        Vlayout.setAlignment(Qt.AlignCenter)

        dialog.setLayout(Vlayout)
        dialog.exec()

    def add_contact_thread(self):
        user_added = self.line_edit_contact_username.text().strip()
        contact_name = self.line_edit_contact_name.text().strip()

        if len(user_added) == 0 or user_added.isspace():
            self.feedback_message.setText("The username can't be empty!")
            self.feedback_message.setStyleSheet("color: red; font-weight: bold;")
            self.feedback_message.setHidden(False)
            return

        if user_added == self.profile["username"]:
            self.feedback_message.setText("You can't add yourself to your contacts. Nice try, though! :)")
            self.feedback_message.setStyleSheet("color: red; font-weight: bold;")
            self.feedback_message.setHidden(False)
            return

        if len(contact_name) == 0 or contact_name.isspace():
            self.feedback_message.setText("You need to specify the contact name!")
            self.feedback_message.setStyleSheet("color: red; font-weight: bold;")
            self.feedback_message.setHidden(False)
            return

        self.uid_from_username_thread = GetUIDByUsernameThread(user_added)
        self.uid_from_username_thread.finished.connect(self.add_contact)
        self.uid_from_username_thread.start()

    def add_contact(self, status_code, response_data):
        if status_code == 200:
            user_uid = self.profile["user_uid"]
            user_added = response_data["user_uid"]
            contact_name = self.line_edit_contact_name.text().strip()

            self.contact_thread = AddContactThread(user_uid, user_added, contact_name)
            self.contact_thread.finished.connect(self.contact_feedback_message)
            self.contact_thread.start()
        
        if status_code == 404:
            self.feedback_message.setStyleSheet("color: red; font-weight: bold;")
            self.feedback_message.setText(f"User not found!")
            self.feedback_message.setHidden(False)
            return

    def contact_feedback_message(self, status_code, response_data):
        if status_code == 201:
            contact_name = response_data["contact_name"]

            self.feedback_message.setStyleSheet("color: green; font-weight: bold;")
            self.feedback_message.setText(f"{contact_name} has been added to your contact list!")
            self.feedback_message.setHidden(False)

            self.populate_contact_list(self.profile["user_uid"])
            return
        
        if status_code == 406:
            self.feedback_message.setStyleSheet("color: red; font-weight: bold;")
            self.feedback_message.setText(f"This user is already in your contact list!")
            self.feedback_message.setHidden(False)
            return

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
        contact_pfp = response_data["profile_picture"]
        image_found = os.path.isfile(os.path.join(utils.PROFILE_IMAGES_FOLDER, contact_pfp))
        if not image_found:
            contact_pfp = "default.png"

        self.current_chat = response_data["user_added"]
        if status_code == 200:
            contact_name = response_data["contact_name"]

            self.ui.label_contact_name.setText(contact_name)
            self.ui.image_contact.setPixmap(QPixmap(os.path.join(utils.PROFILE_IMAGES_FOLDER, contact_pfp)))

        self.clear_messages()
        self.get_conversation()

    def clear_messages(self):
        for i in reversed(range(self.ui.scroll_layout.count())):
            widget = self.ui.scroll_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def get_conversation(self):
        sender = self.profile["user_uid"]
        recipient = self.current_chat

        self.get_conversation_thread = GetConversationThread(sender, recipient)
        self.get_conversation_thread.finished.connect(self.display_conversation)
        self.get_conversation_thread.start()
    
    def display_conversation(self, status_code, response_data):
        # TODO Create a function to not duplicate the same styling block
        if status_code == 200:
            for item in response_data:
                sender = item["sender"]
                message = item["content"]

                alignment = Qt.AlignRight if self.profile["user_uid"] == sender else Qt.AlignLeft

                font = QFont()
                font.setPointSize(11)

                message_label = QLabel(message)
                message_label.setWordWrap(True)
                
                if sender == self.profile["user_uid"]:
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
