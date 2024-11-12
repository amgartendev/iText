from typing import List

from core.deps import get_session
from core.utils import ERROR_MESSAGES
from fastapi import APIRouter, Depends, HTTPException, status
from models.contacts_model import ContactsModel
from models.user_model import UserModel
from schemas.contacts_schema import ContactInfoResponse, ContactsSchemaBase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

router = APIRouter()


# POST Contact
@router.post("/", response_model=ContactsSchemaBase, status_code=status.HTTP_201_CREATED)
async def post_contact(contact: ContactsSchemaBase, db: AsyncSession = Depends(get_session)):
    new_contact: ContactsModel = ContactsModel(
        user_uid=contact.user_uid,
        user_added=contact.user_added,
        contact_name=contact.contact_name
    )

    async with db as session:
        query = select(UserModel).filter(UserModel.user_uid == contact.user_uid)
        result = await session.execute(query)
        user: ContactsModel = result.scalars().one_or_none()

        if not user:
            raise HTTPException(detail=ERROR_MESSAGES["USER_NOT_FOUND"], status_code=status.HTTP_404_NOT_FOUND)

        query = select(UserModel).filter(UserModel.user_uid == contact.user_added)
        result = await session.execute(query)
        user: ContactsModel = result.scalars().one_or_none()

        if not user:
            raise HTTPException(detail=ERROR_MESSAGES["USER_NOT_FOUND"], status_code=status.HTTP_404_NOT_FOUND)

        query = select(ContactsModel).filter(ContactsModel.user_uid == contact.user_uid).filter(ContactsModel.user_added == contact.user_added)
        result = await session.execute(query)
        contact: ContactsModel = result.scalars().one_or_none()

        if contact:
            raise HTTPException(detail=ERROR_MESSAGES["CONTACT_ALREADY_ADDED"], status_code=status.HTTP_406_NOT_ACCEPTABLE)

        session.add(new_contact)
        await session.commit()
        return new_contact


# GET Contacts
@router.get("/{user_uid}", response_model=List[ContactsSchemaBase], status_code=status.HTTP_200_OK)
async def get_contacts(user_uid: str, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel).filter(UserModel.user_uid == user_uid)
        result = await session.execute(query)
        user: UserModel = result.scalars().one_or_none()

        if not user:
            raise HTTPException(detail=ERROR_MESSAGES["USER_NOT_FOUND"], status_code=status.HTTP_404_NOT_FOUND)

        query = select(ContactsModel).filter(ContactsModel.user_uid == user_uid)
        result = await session.execute(query)
        users: List[ContactsModel] = result.scalars().all()
        return users


# GET Contact Info
@router.get("/info/{user_uid}/{user_added}", response_model=ContactInfoResponse, status_code=status.HTTP_200_OK)
async def get_contact_info(user_uid: str, user_added: str, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = (
            select(UserModel, ContactsModel)
            .select_from(ContactsModel)
            .join(UserModel, ContactsModel.user_added == UserModel.user_uid)
            .filter(ContactsModel.user_uid == user_uid)
            .filter(ContactsModel.user_added == user_added)
        )
        result = await session.execute(query)
        data = result.first()

        if data is None:
            return None

        user, contact = data
        return ContactInfoResponse(
            user_uid=user.user_uid,
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            contact_name=contact.contact_name,
            user_added=contact.user_added,
            profile_picture=user.profile_picture
        )
