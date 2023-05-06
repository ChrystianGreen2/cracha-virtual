from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    cor_fundo = Column(String)
    cor_texto = Column(String)
    fonte = Column(String)
    # Adicione outras propriedades visuais conforme necessário

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nfc_id = Column(String, unique=True)
    nome = Column(String)
    email = Column(String)
    celular = Column(String)
    bio = Column(String)
    linkedin = Column(String)
    github = Column(String)
    instagram = Column(String)
    area_profissional = Column(String)
    curso = Column(String)
    universidade = Column(String)
    card_id = Column(Integer, ForeignKey("cards.id"))
    card = relationship("Card")

class UserCreate(BaseModel):
    id: int
    nfc_id: str
    nome: str
    email: EmailStr
    celular: str
    bio: str
    linkedin: str
    github: str
    instagram: str
    area_profissional: str
    curso: str
    universidade: str
    card: dict
