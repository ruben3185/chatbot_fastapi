from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_create_user():
    response = client.post("/init_user/", params={"username": "testuser", "role": "rol de prueba"})
    assert response.status_code == 200
