from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud

router = APIRouter()


@router.get("/")
def read_users(username: str = None, db: Session = Depends(get_db)):
    users = crud.get_users(username, db)
    return users
