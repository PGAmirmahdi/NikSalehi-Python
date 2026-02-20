import sys
import os

from app.database.database import SessionLocal

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.models.User import User
from app.helpers.hash import hash_password


def seed_users(db):
    users = [
        User(
            first_name="Amirmahdi",
            last_name="Asadi",
            email="pgamirmahdi@gmail.com",
            hashed_password=hash_password("1881374"),
        ),
        User(
            first_name="Mohsen",
            last_name="Abedi",
            email="m3abdi@gmail.com",
            hashed_password=hash_password("123456"),
        ),
    ]

    for u in users:
        exists = db.query(User).filter(User.email == u.email).first()
        if not exists:
            db.add(u)

    db.commit()


def main():
    db = SessionLocal()
    try:
        seed_users(db)
        print("✅ با موفقیت دیتا ها سید شدند.")
    finally:
        db.close()


if __name__ == "__main__":
    main()