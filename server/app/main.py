from fastapi import FastAPI
from .database import engine, Base
from .routes import router
from . import models

# Инициализация базы данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Подключение маршрутов
app.include_router(router, prefix="/auth", tags=["Authentication"])