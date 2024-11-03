from core.configs import settings
from sqlalchemy import Column, DateTime, Integer, String


class UserModel(settings.DBBaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_uid = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    username = Column(String(255), unique=True)
    password = Column(String(255))
    created_at = Column(DateTime)
    deleted = Column(Integer, default=0)
