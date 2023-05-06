from fastapi import FastAPI
from .database import Base, engine
from .models.user import User, Card
from .routers.user_router import router as user_router  # Corrigindo a importação

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router, prefix="/api")
