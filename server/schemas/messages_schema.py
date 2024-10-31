from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class MessagesSchemaBase(BaseModel):
    sender: Optional[int] = None  # TODO change to str and get from uid instead of id
    recipient: Optional[int] = None  # TODO change to str and get from uid instead of id
    created_at: Optional[datetime] = None
    content: str

    model_config = ConfigDict(from_attributes=True)


class MessagesSchemaCreate(MessagesSchemaBase):
    id: Optional[int] = None
    message_uid: Optional[str] = None
