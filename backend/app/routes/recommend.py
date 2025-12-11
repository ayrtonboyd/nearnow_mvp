from fastapi import APIRouter
from app.services.llm import run_llm

router = APIRouter()

@router.get("/recommend")
def recommend(query: str):
    response = run_llm(query)
    return {"response": response}
