import qtawesome
from PySide6.QtWidgets import QLineEdit, QMainWindow
from threads import CreateAccountThread
from ui import Ui_MainWindow


class Signup(QMainWindow):
    def __init__(self, ui) -> None:
        self.ui: Ui_MainWindow = ui
        self.is_password_revealed = False
        self.is_confirm_password_revealed = False

        self.ui.button_signup_reveal_password.clicked.connect(lambda: self.toggle_password_visibility(self.ui.input_signup_password, self.ui.button_signup_reveal_password))
        self.ui.button_signup_reveal_confirm_password.clicked.connect(lambda: self.toggle_password_visibility(self.ui.input_signup_confirm_password, self.ui.button_signup_reveal_confirm_password))

        self.signup_form_fields = {
            "first_name": self.ui.input_signup_firstname,
            "last_name": self.ui.input_signup_lastname,
            "username": self.ui.input_signup_username,
            "password": self.ui.input_signup_password,
            "confirm_password": self.ui.input_signup_confirm_password
        }

        self.error_messages = {
            "first_name": self.ui.label_error_message_firstname,
            "last_name": self.ui.label_error_message_lastname,
            "username": self.ui.label_error_message_username,
            "password": self.ui.label_error_message_password,
            "confirm_password": self.ui.label_error_message_confirm_password
        }

    def initiate_account_creation(self) -> None:
        """
        Validates the input fields for account creation and displays error messages if any
        field is invalid. Start a thread to create a new account.

        Validation rules:
        - First name cannot be empty or contain only whitespace.
        - Last name cannot be empty or contain only whitespace.
        - Username cannot be empty or contain only whitespace.
        - Password must be at least 6 characters long and cannot be empty or contain only whitespace.
        - Password and confirmation password must match.
        """
        first_name = self.ui.input_signup_firstname.text().strip()
        last_name = self.ui.input_signup_lastname.text().strip()
        username = self.ui.input_signup_username.text().strip()
        password = self.ui.input_signup_password.text().strip()
        confirm_password = self.ui.input_signup_confirm_password.text().strip()

        self.errors = {}

        if len(first_name) == 0 or first_name.isspace():
            self.errors["first_name"] = "First name cannot be empty."

        if len(last_name) == 0 or last_name.isspace():
            self.errors["last_name"] = "Last name cannot be empty."

        if len(username) == 0 or username.isspace():
            self.errors["username"] = "Username cannot be empty."

        if len(password) < 6:
            self.errors["password"] = "Password must be at least 6 characters long."

        if len(password) == 0 or password.isspace():
            self.errors["password"] = "Password cannot be empty."

        if password != confirm_password:
            self.errors["confirm_password"] = "Passwords do not match."

        self.clear_previous_error_messages()
        self.show_error_messages()
        
        if not self.errors:
            self.create_account_thread = CreateAccountThread(first_name, last_name, username, password)
            self.create_account_thread.finished.connect(self.create_account)
            self.create_account_thread.start()
    
    def create_account(self, status_code: int, response_data: dict) -> None:
        """
        Redirects to the login page if the account is successfully created.

        Args:
            status_code (int): The HTTP status code from the account creation request.
            response_data (dict): Data containing the account that was created, if  the account
                                  was successfully created.
        """
        if status_code == 201:
            self.clear_input_fields()
            self.ui.label_signup_success_message.setHidden(False)
        
        if status_code == 406:
            self.errors["username"] = "The username is already taken."
            self.show_error_messages()
            return

    def clear_input_fields(self) -> None:
        """
        Clears all input fields in the signup form.
        """
        for field in self.signup_form_fields.values():
            field.clear()

    def clear_previous_error_messages(self) -> None:
        """
        Hides all error message labels to reset the form's error display.
        """
        for field in self.error_messages.values():
            field.setHidden(True)

    def show_error_messages(self) -> None:
        """
        Displays error message for invalid fields in the form.
        """
        for field, message in self.errors.items():
            error_label = self.error_messages[field]
            error_label.setText(message)
            error_label.setHidden(False)
    
    def toggle_password_visibility(self, field: QLineEdit, icon_button) -> None:
        """
        Toggles the password visibility and updates the eye icon
        in the signup page based on the current state.
        """
        if field == self.ui.input_signup_password:
            is_revealed = self.is_password_revealed
        elif field == self.ui.input_signup_confirm_password:
            is_revealed = self.is_confirm_password_revealed
        else:
            return

        # Toggle visibility based on current state
        if not is_revealed:
            field.setEchoMode(QLineEdit.EchoMode.Normal)
            icon_button.setIcon(qtawesome.icon("fa5.eye-slash", color="#007AFF"))
            if field == self.ui.input_signup_password:
                self.is_password_revealed = True
            else:
                self.is_confirm_password_revealed = True
        else:
            field.setEchoMode(QLineEdit.EchoMode.Password)
            icon_button.setIcon(qtawesome.icon("fa5.eye", color="#007AFF"))
            if field == self.ui.input_signup_password:
                self.is_password_revealed = False
            else:
                self.is_confirm_password_revealed = False
