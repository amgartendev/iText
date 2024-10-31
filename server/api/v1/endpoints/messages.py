from datetime import datetime
from typing import List
from uuid import uuid4

from core.deps import get_session
from core.utils import ERROR_MESSAGES
from fastapi import APIRouter, Depends, HTTPException, status
from models.messages_model import MessagesModel
from models.user_model import UserModel
from schemas.messages_schema import MessagesSchemaBase, MessagesSchemaCreate
from sqlalchemy import or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

router = APIRouter()


# POST Create message
@router.post("/{sender_id}/{recipient_id}", response_model=MessagesSchemaBase, status_code=status.HTTP_201_CREATED)
async def post_message(sender_id: int, recipient_id: int, message_data: MessagesSchemaCreate, db: AsyncSession = Depends(get_session)):    
    new_message: MessagesModel = MessagesModel(
        message_uid=str(uuid4()),
        sender=sender_id,
        recipient=recipient_id,
        created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        content=message_data.content
    )
    async with db as session:
        # Check if sender exists
        query = select(UserModel).filter(UserModel.id == sender_id)
        result = await session.execute(query)
        sender: UserModel = result.scalars().one_or_none()

        if not sender:
            raise HTTPException(detail=ERROR_MESSAGES["SENDER_NOT_FOUND"], status_code=status.HTTP_404_NOT_FOUND)

        # Check if recipient exists
        query = select(UserModel).filter(UserModel.id == recipient_id)
        result = await session.execute(query)
        recipient: UserModel = result.scalars().one_or_none()

        if not recipient:
            raise HTTPException(detail=ERROR_MESSAGES["RECIPIENT_NOT_FOUND"], status_code=status.HTTP_404_NOT_FOUND)

        session.add(new_message)
        await session.commit()
        return new_message


# GET messages from user
@router.get("/{user_id}", response_model=List[MessagesSchemaBase], status_code=status.HTTP_200_OK)
async def get_messages(user_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel).filter(UserModel.id == user_id)
        result = await session.execute(query)
        user: UserModel = result.scalars().one_or_none()

        if not user:
            raise HTTPException(detail=ERROR_MESSAGES["USER_NOT_FOUND"], status_code=status.HTTP_404_NOT_FOUND)

        query = select(MessagesModel).filter(or_(MessagesModel.sender == user_id, MessagesModel.recipient == user_id))
        result = await session.execute(query)
        messages: List[MessagesModel] = result.scalars().all()
        return messages


# GET message
@router.get("/message/{message_uid}", response_model=MessagesSchemaBase, status_code=status.HTTP_200_OK)
async def get_message(message_uid: str, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MessagesModel).filter(MessagesModel.message_uid == message_uid)
        result = await session.execute(query)
        message: MessagesModel = result.scalars().one_or_none()

        if not message:
            raise HTTPException(detail=ERROR_MESSAGES["MESSAGE_NOT_FOUND"], status_code=status.HTTP_404_NOT_FOUND)
        return message
