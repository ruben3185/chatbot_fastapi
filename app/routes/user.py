from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models.models import User
from app.utils.database import engine

router = APIRouter()

@router.post("/")
def create_user(username: str, role: str):
    with Session(engine) as session:
        existing_user = session.exec(select(User).where(User.username == username)).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Usuario ya existe")

        user = User(username=username, role=role)
        session.add(user)
        session.commit()
        return {"message": "Usuario creado"}
