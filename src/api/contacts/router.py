from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud

router = APIRouter()


@router.get("/")
def read_contacts(db: Session = Depends(get_db)):
    contacts = crud.get_contacts(db)
    return contacts


@router.post("/add_contact")
def add_contact(user_uid, contact_uid, contact_name, db: Session = Depends(get_db)):
    add_contact = crud.add_contact(db, user_uid, contact_uid, contact_name)
    return add_contact
