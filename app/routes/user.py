from fastapi import APIRouter, HTTPException
from sqlmodel import Session
from app.models.models import User
from app.utils.database import engine

router = APIRouter()

@router.post("/")
def create_user(username: str, role: str):
    with Session(engine) as session:
        if session.query(User).filter_by(username=username).first():
            raise HTTPException(status_code=400, detail="Usuario ya existe")
        user = User(username=username, role=role)
        session.add(user)
        session.commit()
        return {"message": "Usuario creado"}
