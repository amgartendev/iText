import os

from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel

API_URL = os.environ.get("API_URL")
PROJECT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
)


def custom_dialog(parent, message=None):
    layout = QVBoxLayout()
    error_dialog = QDialog(parent)
    error_label = QLabel(message)
    layout.addWidget(error_label)
    error_dialog.setLayout(layout)
    error_dialog.exec()
