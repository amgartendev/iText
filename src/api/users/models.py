from database import Base
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    unique_id = Column(String(36), unique=True, index=True)
    first_name = Column(String(128))
    last_name = Column(String(128))
    username = Column(String(64), unique=True, index=True)
    email = Column(String(128), unique=True, index=True)
    created_at = Column(DateTime, server_default=func.now())
