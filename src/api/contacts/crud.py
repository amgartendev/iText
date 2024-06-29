import json

from sqlalchemy.orm import Session

from . import models, schemas


def get_contacts(db: Session, user_uid):
    if user_uid:
        return (
            db.query(models.Contacts)
            .filter(models.Contacts.user_uid == user_uid)
            .first()
        )
    return db.query(models.Contacts).all()


def add_contact(
    db: Session, user_uid: str, contact_uid: str, contact_name: str) -> None:
    contacts_obj = get_contacts(db, user_uid)
    new_contact = {contact_uid: contact_name}

    if contacts_obj:
        contacts_list = json.loads(contacts_obj.contacts)
        contacts_list.append(new_contact)
        contacts_obj.contacts = json.dumps(contacts_list)
    else:
        contacts_data = schemas.ContactsBase(
            user_uid=user_uid, contacts=json.dumps([new_contact])
        )
        db.add(models.Contacts(**contacts_data.model_dump()))

    db.commit()
