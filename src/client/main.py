import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
)

import contacts
from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout
from ui import *

import utils

UID_TEST_TOKEN = os.environ.get("UID_TEST_TOKEN")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        contacts.populate(self.ui, UID_TEST_TOKEN)
        self.ui.pushButton_add_contact.clicked.connect(self.add_contact)

    def add_contact(self):
        dialog = QDialog()
        layout = QVBoxLayout(dialog)
        contact_username_lineEdit = QLineEdit()
        contact_name_lineEdit = QLineEdit()
        contact_username_lineEdit.setPlaceholderText("Username")
        contact_name_lineEdit.setPlaceholderText("Contact name")
        add_contact = QPushButton("Add Contact")
        layout.addWidget(contact_username_lineEdit)
        layout.addWidget(contact_name_lineEdit)
        layout.addWidget(add_contact)

        def handle_add_contact():
            contact_username = contact_username_lineEdit.text()
            contact_name = contact_name_lineEdit.text()
            # Check if username is already in the contact list
            for index in range(self.ui.listWidget_contacts.count()):
                contact = self.ui.listWidget_contacts.item(index)
                if contact_username == contact.text():
                    dialog.close()
                    utils.custom_dialog(self, "This person is already in your contact list.")
                    return

            response = contacts.add(contact_username, contact_name)
            if not response:
                dialog.close()
                utils.custom_dialog(self, "An error occurred.")
                return

            self.ui.listWidget_contacts.clear()
            contacts.populate(self.ui, UID_TEST_TOKEN, update=True)
            dialog.accept()

        add_contact.clicked.connect(handle_add_contact)
        dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
