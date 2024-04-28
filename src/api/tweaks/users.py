from datetime import date

from database import SessionLocal
from faker import Faker

from users.models import User


def populate_test_users(count: int):
    db = SessionLocal()
    fake = Faker()
    test_user_ids = []

    for i in range(count):
        test_user = User(
            unique_id=fake.unique.uuid4(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            username=fake.unique.user_name(),
            email=fake.unique.email(),
            created_at=fake.date_between_dates(
                date_start=date(year=1960, month=1, day=1),
                date_end=date(year=2005, month=12, day=30),
            ),
        )
        db.add(test_user)
        test_user_ids.append(test_user.id)

    db.commit()
    return test_user_ids
