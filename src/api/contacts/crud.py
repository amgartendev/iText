from sqlalchemy import insert
from sqlalchemy.orm import Session

from . import models, schemas


def get_contacts(db: Session):
    return db.query(models.Contacts).all()


def add_contact(db: Session, user_uid, contact_uid, contact_name):
    contacts_table = models.Contacts

    contact_data = schemas.ContactsBase(
        user_uid=user_uid, contacts=str([{contact_uid: {"saved_as": contact_name}}])
    )

    query = insert(contacts_table).values(
        user_uid=contact_data.user_uid,
        contacts=contact_data.contacts,
    )

    db.execute(query)
    db.commit()
