from datetime import datetime
from typing import List
from uuid import uuid4

from core.deps import get_session
from core.utils import ERROR_MESSAGES
from fastapi import APIRouter, Depends, HTTPException, status
from models.messages_model import MessagesModel
from models.user_model import UserModel
from schemas.messages_schema import MessagesSchemaBase, MessagesSchemaCreate
from sqlalchemy import and_, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

router = APIRouter()


# POST Create message
@router.post("/{sender_uid}/{recipient_uid}", response_model=MessagesSchemaBase, status_code=status.HTTP_201_CREATED)
async def post_message(sender_uid: str, recipient_uid: str, message_data: MessagesSchemaCreate, db: AsyncSession = Depends(get_session)):    
    async with db as session:
        # Check if sender exists
        query = select(UserModel.user_uid).filter(UserModel.user_uid == sender_uid)
        result = await session.execute(query)
        sender: UserModel = result.scalars().one_or_none()

        if not sender:
            raise HTTPException(detail=ERROR_MESSAGES["SENDER_NOT_FOUND"], status_code=status.HTTP_404_NOT_FOUND)

        # Check if recipient exists
        query = select(UserModel.user_uid).filter(UserModel.user_uid == recipient_uid)
        result = await session.execute(query)
        recipient: UserModel = result.scalars().one_or_none()

        if not recipient:
            raise HTTPException(detail=ERROR_MESSAGES["RECIPIENT_NOT_FOUND"], status_code=status.HTTP_404_NOT_FOUND)

        new_message: MessagesModel = MessagesModel(
            message_uid=str(uuid4()),
            sender=sender,
            recipient=recipient,
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            content=message_data.content
        )

        session.add(new_message)
        await session.commit()
        return new_message


# GET messages from user
@router.get("/{user_uid}", response_model=List[MessagesSchemaBase], status_code=status.HTTP_200_OK)
async def get_messages(user_uid: str, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel).filter(UserModel.user_uid == user_uid)
        result = await session.execute(query)
        user: UserModel = result.scalars().one_or_none()

        if not user:
            raise HTTPException(detail=ERROR_MESSAGES["USER_NOT_FOUND"], status_code=status.HTTP_404_NOT_FOUND)

        query = select(MessagesModel).filter(or_(MessagesModel.sender == user_uid, MessagesModel.recipient == user_uid))
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


# GET Conversation
@router.get("/conversation/{sender_uid}/{recipient_uid}", response_model=List[MessagesSchemaBase], status_code=status.HTTP_200_OK)
async def get_conversation(sender_uid: str, recipient_uid: str, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = (
            select(MessagesModel)
            .where(
                or_(
                    and_(
                        MessagesModel.sender == sender_uid,
                        MessagesModel.recipient == recipient_uid
                    ),
                    and_(
                        MessagesModel.sender == recipient_uid,
                        MessagesModel.recipient == sender_uid
                    )
                )
            )
        )
        result = await session.execute(query)
        messages: MessagesModel = result.scalars().all()
        return messages
