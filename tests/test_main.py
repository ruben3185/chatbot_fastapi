import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from main import app
from sqlmodel import Session, select
from app.models.models import User
from app.utils.database import engine

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_create_user():
    username = "testuser"
    role = "rol de prueba"

    # Elimina si el usuario ya existe
    with Session(engine) as session:
        existing_user = session.exec(select(User).where(User.username == username)).first()
        if existing_user:
            session.delete(existing_user)
            session.commit()

    # Crea el usuario
    response = client.post("/init_user/", params={"username": username, "role": role})
    assert response.status_code == 200
    assert response.json() == {"message": "Usuario creado"}
