from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os

# Конструирует ссылку для подключения к бд
def get_db_url():
    POSTGRES_PORT = os.getenv('POSTGRES_PORT')
    POSTGRES_SERVER = os.getenv('POSTGRES_SERVER')
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_DB = os.getenv('POSTGRES_DB')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD_FILE')
    with open(POSTGRES_PASSWORD, 'r') as file:
        POSTGRES_PASSWORD = file.read().strip()
    return f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'

# class Base(DeclarativeBase):
#     pass

Base = declarative_base()

DATABASE_URL = get_db_url()

engine = create_engine(url=DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()