from fastapi import APIRouter
from app.services.llm import run_llm
from app.services.data_loader import load_locations, load_tags
from app.services.test_runner import run_all_validations, save_test_result

router = APIRouter()

@router.get("/run_test")
def run_test(question: str):
    dataset = {
        "locations": load_locations(),
        "tags": load_tags()
    }

    answer = run_llm(question)

    final_score, results = run_all_validations(
        question,
        answer,
        dataset
    )

    saved_path = save_test_result(question, answer, final_score, results)

    return {
        "question": question,
        "answer": answer,
        "final_score": final_score,
        "details": results,
        "saved_to": saved_path
    }
