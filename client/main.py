import sys

from login_ui import Ui_MainWindow
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("iText - Login component")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.setWindowFlags(window.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
    window.show()
    app.exec()
