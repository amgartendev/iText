from pydantic import BaseModel, ConfigDict


class ContactsSchemaBase(BaseModel):
    user_uid: str
    user_added: str
    contact_name: str

    model_config = ConfigDict(from_attributes=True)
