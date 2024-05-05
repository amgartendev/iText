import ast
import json
import os

import requests
from dotenv import load_dotenv

from utils import API_URL, PROJECT_PATH

loaded_dotenv = load_dotenv()


def populate(ui, user_uid):
    contacts_cache = os.path.isfile(f"{PROJECT_PATH}/contacts")
    if contacts_cache:
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


def add():
    pass
