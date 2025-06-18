from fastapi import APIRouter, HTTPException
from sqlmodel import Session
from app.models.models import Message, User
from app.utils.database import engine
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

@router.post("/ask")
def ask_question(username: str, question: str):
    with Session(engine) as session:
        user = session.query(User).filter_by(username=username).first()
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        api_key = os.getenv("OPENAI_API_KEY")

        try:
            response = httpx.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {api_key}"},
                json={
                    "model": "gpt-3.5-turbo",
                    "messages": [{"role": "system", "content": user.role},
                                 {"role": "user", "content": question}]
                }
            )
            data = response.json()
            answer = data["choices"][0]["message"]["content"]
            answer = "hola"
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

        msg = Message(username=username, question=question, response=answer)
        session.add(msg)
        session.commit()
        return {"response": answer}

@router.get("/history/{username}")
def get_history(username: str):
    with Session(engine) as session:
        messages = session.query(Message).filter_by(username=username).all()
        return [{"question": m.question, "response": m.response} for m in messages]
