from pydantic import BaseModel

class ContactsBase(BaseModel):
    user_uid: str
    contacts: str
