from api.v1.endpoints import contacts, messages, users
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(contacts.router, prefix="/contacts", tags=["Contacts"])
api_router.include_router(messages.router, prefix="/messages", tags=["Messages"])
