import os
import sys

import pygame
import requests
import utils
from messages_ui import Ui_MainWindow
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
                               QVBoxLayout, QWidget)


class Messages(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("iText - Messages component")

        self.messages = [
            ("Hey, what's up?", True),
            ("Nothing much, just watching a movie", False),
            ("Hey, did you see the concert that will happen tomorrow? 👀", False),
        ]
        self.current_message_index = 0

        # Inicializa o layout do scrollAreaWidgetContents
        self.ui.scrollAreaWidgetContents.setLayout(QVBoxLayout())

        # TODO Remove the timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_next_message)
        self.timer.start(2000)  # 2000 ms = 2 segundos

    def show_next_message(self):
        if self.current_message_index < len(self.messages):
            text, align_right = self.messages[self.current_message_index]
            self.add_message(text, align_right)
            self.current_message_index += 1
        else:
            self.timer.stop()

    def add_message(self, text, align_right=False):
        payload = {"content": text}
        request = requests.post(f"{utils.API_URL}/{utils.API_BASE_ENDPOINT}/1/2", json=payload)
        """
        container_widget = QWidget()
        container_layout = QHBoxLayout(container_widget)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(5)

        message_label = QLabel(text, container_widget)
        if align_right:
            message_label.setStyleSheet("font-size: 16px; background-color: #1C8AFF; color: #FFFFFF; padding: 10px; border-radius: 5px;")
        else:
            message_label.setStyleSheet("font-size: 16px; background-color: #E8E8EB; color: #101010; padding: 10px; border-radius: 5px;")
        message_label.setWordWrap(True)
        message_label.setMinimumWidth(300)
        message_label.setMaximumHeight(100)

        if align_right:
            container_layout.addStretch()
            container_layout.addWidget(message_label, alignment=Qt.AlignRight)
            pygame.mixer.init()
            pygame.mixer.music.load(os.path.join(utils.AUDIO_FOLDER, 'SentMessage.wav'))
            pygame.mixer.music.play()
        else:
            container_layout.addWidget(message_label, alignment=Qt.AlignLeft)
            container_layout.addStretch()
            pygame.mixer.init()
            pygame.mixer.music.load(os.path.join(utils.AUDIO_FOLDER, 'ReceivedMessage.wav'))
            pygame.mixer.music.play()

        self.ui.scrollAreaWidgetContents.layout().addWidget(container_widget)
        self.ui.scrollArea.verticalScrollBar().setValue(self.ui.scrollArea.verticalScrollBar().maximum())
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Messages()
    window.show()
    app.exec()
