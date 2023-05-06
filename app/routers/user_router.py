from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..models.user import User, UserCreate  # Corrigindo a importação
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/cadastro/{user_id}")
async def create_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.id == user_id).first():
        raise HTTPException(status_code=400, detail="ID já cadastrado")

    # Criando uma instância do modelo ORM User e preenchendo com os dados do modelo Pydantic UserCreate
    user_orm = User(
        id=user_id,
        nfc_id=user.nfc_id,
        nome=user.nome,
        email=user.email,
        celular=user.celular,
        bio=user.bio,
        linkedin=user.linkedin,
        github=user.github,
        instagram=user.instagram,
        area_profissional=user.area_profissional,
        curso=user.curso,
        universidade=user.universidade,
    )

    db.add(user_orm)
    db.commit()
    db.refresh(user_orm)
    return {"msg": "Usuário cadastrado com sucesso"}


@router.get("/busca/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()  # Corrigindo a referência à classe User
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user

@router.get("/busca_nfc/{nfc_id}")
async def read_user_by_nfc(nfc_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.nfc_id == nfc_id).first()  # Corrigindo a referência à classe User
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user
