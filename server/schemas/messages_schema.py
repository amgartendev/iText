from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class MessagesSchemaBase(BaseModel):
    sender: Optional[str] = None
    recipient: Optional[str] = None
    created_at: Optional[datetime] = None
    content: str

    model_config = ConfigDict(from_attributes=True)


class MessagesSchemaCreate(MessagesSchemaBase):
    id: Optional[int] = None
    message_uid: Optional[str] = None
