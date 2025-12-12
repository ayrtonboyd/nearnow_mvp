from fastapi import APIRouter
from app.services.llm import run_llm

router = APIRouter()

@router.get("/recommend")
def recommend(query: str):
    answer = run_llm(query)
    return {"answer": answer}
