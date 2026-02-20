from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:root1234@localhost:3306/python-project?charset=utf8mb4"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,     # قبل از استفاده از هر connection، یه ping ساده به دیتابیس می‌زنه. اگر connection مرده باشه یه connection جدید میسازه.
    pool_recycle=3600,      # MySQL معمولاً بعد از یه مدت idle بودن connection رو می‌بنده.
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
