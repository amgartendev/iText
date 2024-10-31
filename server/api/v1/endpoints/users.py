from datetime import datetime
from typing import List
from uuid import uuid4

from core.deps import get_session
from core.utils import ERROR_MESSAGES
from fastapi import APIRouter, Depends, HTTPException, Response, status
from models.user_model import UserModel
from schemas.user_schema import (UserSchemaBase, UserSchemaCreate,
                                 UserSchemaUpdate)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


router = APIRouter()


# Post User
@router.post("/", response_model=UserSchemaBase, status_code=status.HTTP_201_CREATED)
async def post_user(user: UserSchemaCreate, db: AsyncSession = Depends(get_session)):
    new_user: UserModel = UserModel(
        user_uid=str(uuid4()),
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        password=user.password,
        created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        deleted=user.deleted,
    )
    async with db as session:
        session.add(new_user)
        await session.commit()
        return new_user


# GET Users
@router.get("/", response_model=List[UserSchemaBase], status_code=status.HTTP_200_OK)
async def get_users(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel)
        result = await session.execute(query)
        users: List[UserModel] = result.scalars().all()
        return users


# GET User
@router.get("/{user_id}", response_model=UserSchemaBase, status_code=status.HTTP_200_OK)
async def get_user(user_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel).filter(UserModel.id == user_id)
        result = await session.execute(query)
        user: UserModel = result.scalars().one_or_none()

        if not user:
            raise HTTPException(detail=ERROR_MESSAGES["USER_NOT_FOUND"], status_code=status.HTTP_404_NOT_FOUND)
        return user


# PUT Update Profile
@router.put("/{user_id}", response_model=UserSchemaBase, status_code=status.HTTP_202_ACCEPTED)
async def put_profile(user_id: int, user: UserSchemaUpdate, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel).filter(UserModel.id == user_id)
        result = await session.execute(query)
        user_update: UserModel = result.scalars().one_or_none()

        if not user_update:
            raise HTTPException(detail=ERROR_MESSAGES["USER_NOT_FOUND"], status_code=status.HTTP_404_NOT_FOUND)

        if user.first_name:
            user_update.first_name = user.first_name
        
        if user.last_name:
            user_update.last_name = user.last_name
        
        if user.username:
            user_update.username = user.username
        
        if user.password:
            user_update.password = user.password

        await session.commit()
        return user_update


# PUT Update Deleted Flag
@router.put("/delete/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def put_deleted_flag(user_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel).filter(UserModel.id == user_id)
        result = await session.execute(query)
        update: UserModel = result.scalars().one_or_none()

        if not update:
            raise HTTPException(detail=ERROR_MESSAGES["USER_NOT_FOUND"], status_code=status.HTTP_404_NOT_FOUND)

        update.deleted = 1
        await session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
