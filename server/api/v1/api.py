from api.v1.endpoints import messages, users
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(messages.router, prefix="/messages", tags=["Messages"])
