from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class UserSchemaBase(BaseModel):
    user_uid: Optional[str] = None
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None
    profile_picture: Optional[str] = None
    created_at: Optional[datetime] = None
    deleted: Optional[int] = 0

    model_config = ConfigDict(from_attributes=True)


class UserSchemaCreate(UserSchemaBase):
    id: Optional[int] = None
    username: str
    password: str


class UserSchemaUpdate(UserSchemaCreate):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None


class UserSchemaLogin(BaseModel):
    username: str
    password: str 


class UserSchemaUsername(BaseModel):
    username: str
    user_uid: str
