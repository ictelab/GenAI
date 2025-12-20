### api.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.llm.byllm_client import ask_llm
from jaseci import Jaseci

router = APIRouter()
js = Jaseci()
js.load("app/jac/learning.jac")

class Prompt(BaseModel):
    question: str

@router.post("/chat")
def chat(prompt: Prompt):
    answer = ask_llm(prompt.question)
    return {"response": answer}
