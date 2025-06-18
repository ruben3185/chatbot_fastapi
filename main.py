from fastapi import FastAPI
from app.routes.user import router as user_router
from app.routes.chatbot import router as chatbot_router
from app.routes.health import router as health_router
from app.utils.database import init_db

app = FastAPI(title="Chatbot FastAPI")

init_db()

app.include_router(user_router, prefix="/init_user", tags=["Users"])
app.include_router(chatbot_router, tags=["Chatbot"])
app.include_router(health_router, tags=["Health"])
