from database import Base
from sqlalchemy import Column, Integer, String


class Contacts(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)
    user_uid = Column(String(36), unique=True, index=True)
    contacts = Column(String(280), index=True)
