from sqlalchemy.orm import Session

from . import models


def get_users(username, db: Session):
    if username is None:
        return db.query(models.User).all()
    return db.query(models.User).filter(models.User.username == username).first()
