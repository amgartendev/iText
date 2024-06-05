import ast
import json
import os

from custom_exceptions import EndpointException
import requests
from dotenv import load_dotenv

from utils import API_URL, PROJECT_PATH

UID_TEST_TOKEN = os.environ.get("UID_TEST_TOKEN")
loaded_dotenv = load_dotenv()


def populate(ui, user_uid, update=False):
    contacts_cache = os.path.isfile(f"{PROJECT_PATH}/contacts")
    if contacts_cache and not update:
        with open(f"{PROJECT_PATH}/contacts", "r") as file:
            contacts_data = file.read()
            if contacts_data:
                try:
                    contacts = json.loads(contacts_data)
                    for data in contacts:
                        for contact in data.values():
                            ui.listWidget_contacts.addItem(contact)
                except json.JSONDecodeError:
                    print("Error: Invalid JSON data in contacts file.")
    else:
        try:
            response = requests.get(API_URL + "contacts/?user_uid=" + user_uid)
            if response.status_code == 200:
                result = response.json()
                contacts_list: list = ast.literal_eval(result["contacts"])

                for data in contacts_list:
                    for contact in data.values():
                        ui.listWidget_contacts.addItem(contact)

                with open(f"{PROJECT_PATH}/contacts", "w") as file:
                    json.dump(contacts_list, file, indent=4)
        except Exception as error_message:
            return error_message


def add(contact_username, contact_name):
    try:
        # Check if the user exists by its username
        check_user_response = requests.get(
            API_URL + f"users?username={contact_username}"
        )
        if check_user_response.status_code != 200:
            raise Exception("Something went wrong.")

        if check_user_response.json() is None:
            raise Exception("This person does not exists!")

        contact_uid = check_user_response.json()["unique_id"]

        # Add the user to the contacts, get the contact_uid by its username
        response = requests.post(
            API_URL
            + f"contacts/add_contact?user_uid={UID_TEST_TOKEN}&contact_uid={contact_uid}&contact_name={contact_name}"
        )
        if response.status_code == 200:
            return True
    except Exception as error_message:
        raise Exception(error_message)
