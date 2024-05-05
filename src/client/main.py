import os
import sys

sys.path.append("/Users/amgarten/Desktop/Code/Python/iText/src/")
sys.path.append("/Users/amgarten/Desktop/Code/Python/iText/src/api/")

import contacts
from ui import *

UID_TEST_TOKEN = os.environ.get("UID_TEST_TOKEN")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        contacts.populate(self.ui, UID_TEST_TOKEN)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
