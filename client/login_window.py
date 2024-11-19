import sys

import qtawesome
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow
from threads import LoginThread
from ui import Ui_MainWindow


class Login(QMainWindow):
    login_finished = Signal(int, dict)

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("iText - Login")
        self.setFixedSize(800, 600)
        self.is_password_revealed = False
        self.running_thread = False

        # Setup UI connections
        self.ui.button_reveal_password.clicked.connect(self.toggle_password_visibility)
        self.ui.button_login.clicked.connect(self.initiate_login)

    def toggle_password_visibility(self) -> None:
        """
        Toggles the password visibility and updates the eye icon
        in the login page based on the current state.
        """
        if not self.is_password_revealed:
            self.ui.input_password.setEchoMode(QLineEdit.EchoMode.Normal)
            self.ui.button_reveal_password.setIcon(qtawesome.icon('fa5.eye-slash', color="#007AFF"))
            self.is_password_revealed = True
        else:
            self.ui.input_password.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.button_reveal_password.setIcon(qtawesome.icon('fa5.eye', color="#007AFF"))
            self.is_password_revealed = False

    def initiate_login(self) -> None:
        """
        Starts the login process by creating and running the LoginThread with
        the provided username and password.
        """
        if self.running_thread:
            return
        username = self.ui.input_username.text()
        password = self.ui.input_password.text()

        self.login_thread = LoginThread(username, password)
        self.login_thread.finished.connect(self.on_login_finished)
        self.login_thread.start()
        self.running_thread = True

    def on_login_finished(self, status_code: int, response_data: dict) -> None:
        """
        Handles the completion of the login process. Emits a success signal if
        login is successful; otherwise, displays an error message.

        Args:
            status_code (int): HTTP status code returned by the login attempt.
            response_data (dict): Data returned from the login attempt, containing additional information on failure.
        """
        self.running_thread = False
        if status_code == 200:
            self.login_finished.emit(status_code, response_data)
        else:
            self.ui.label_error_message.setText(response_data.get("detail", "Login failed"))
            self.ui.label_error_message.setVisible(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()
