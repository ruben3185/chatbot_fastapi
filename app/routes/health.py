from fastapi import APIRouter
from app.utils.database import engine
from sqlalchemy import text  # ← IMPORTANTE

router = APIRouter()

@router.get("/health")
def health_check():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))  # ← FIX AQUÍ
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "details": str(e)}
