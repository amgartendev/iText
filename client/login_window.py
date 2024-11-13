import sys

import qtawesome
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow
from threads import LoginThread
from ui import Ui_MainWindow


class Login(QMainWindow):
    login_finished = Signal(int, dict)

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("iText - Login")
        self.is_password_revealed = False
        self.running_thread = False

        # Setup UI connections
        self.ui.button_reveal_password.clicked.connect(self.toggle_password_visibility)
        self.ui.button_login.clicked.connect(self.initiate_login)

    def toggle_password_visibility(self):
        if not self.is_password_revealed:
            self.ui.input_password.setEchoMode(QLineEdit.EchoMode.Normal)
            self.ui.button_reveal_password.setIcon(qtawesome.icon('fa5.eye-slash', color="#007AFF"))
            self.is_password_revealed = True
        else:
            self.ui.input_password.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.button_reveal_password.setIcon(qtawesome.icon('fa5.eye', color="#007AFF"))
            self.is_password_revealed = False

    def initiate_login(self):
        if self.running_thread:
            return
        username = self.ui.input_username.text()
        password = self.ui.input_password.text()

        self.login_thread = LoginThread(username, password)
        self.login_thread.finished.connect(self.on_login_finished)
        self.login_thread.start()
        self.running_thread = True

    def on_login_finished(self, status_code, response_data):
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
