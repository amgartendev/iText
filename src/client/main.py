import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
)

import contacts
from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout
from ui import *

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
                    layout = QVBoxLayout()
                    error_dialog = QDialog(self)
                    error_label = QLabel("This person is already in your contact list.")
                    layout.addWidget(error_label)
                    error_dialog.setLayout(layout)
                    error_dialog.exec()
                    return

            response = contacts.add(contact_username, contact_name)
            if not response:
                dialog.close()
                layout = QVBoxLayout()
                error_dialog = QDialog(self)
                error_label = QLabel("An error occurred.")
                layout.addWidget(error_label)
                error_dialog.setLayout(layout)
                error_dialog.exec()
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
