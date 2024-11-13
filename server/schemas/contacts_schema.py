from pydantic import BaseModel, ConfigDict


class ContactsSchemaBase(BaseModel):
    user_uid: str
    user_added: str
    contact_name: str

    model_config = ConfigDict(from_attributes=True)


class ContactInfoResponse(BaseModel):
    user_uid: str
    first_name: str
    last_name: str
    username: str
    contact_name: str
    user_added: str
    profile_picture: str

    model_config = ConfigDict(from_attributes=True)
