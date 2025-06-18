from fastapi import APIRouter
from app.utils.database import engine

router = APIRouter()

@router.get("/health")
def health_check():
    try:
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "details": str(e)}
