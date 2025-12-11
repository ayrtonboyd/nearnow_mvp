from fastapi import APIRouter
from app.services.bulk_test_runner import run_bulk_tests

router = APIRouter()

@router.get("/run_all_tests")
def run_all_tests():
    summary, results, path = run_bulk_tests()

    return {
        "summary": summary,
        "test_results_saved_to": path
    }
