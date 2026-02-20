from sqlalchemy import Column, Integer, String, DateTime, func

from app.database.database import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {
        "mysql_charset": "utf8mb4",
        "mysql_collate": "utf8mb4_unicode_ci",
    }

    id = Column(Integer, primary_key=True)

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=True)

    email = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())