from sqlalchemy import event
from database import Base
from . import users


def create_test_values(target, connection, **kw):
    user_count = 50
    users.populate_test_users(user_count)


def listen_for_events():
    event.listen(Base.metadata, "after_create", create_test_values)
