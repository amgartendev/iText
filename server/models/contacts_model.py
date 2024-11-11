from core.configs import settings
from sqlalchemy import Column, Integer, String


class ContactsModel(settings.DBBaseModel):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_uid = Column(String(255))
    user_added = Column(String(255))
    contact_name = Column(String(255))
