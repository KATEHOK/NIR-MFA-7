from fastapi import FastAPI
from .database import engine, Base
from . import routes

# Инициализация базы данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Подключение маршрутов
app.include_router(routes.router, prefix="/auth", tags=["Authentication"])