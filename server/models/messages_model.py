from core.configs import settings
from sqlalchemy import Column, DateTime, Integer, String


class MessagesModel(settings.DBBaseModel):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    message_uid = Column(String(255))
    sender = Column(String(255))
    recipient = Column(String(255))
    created_at = Column(DateTime)
    content = Column(String(500))
