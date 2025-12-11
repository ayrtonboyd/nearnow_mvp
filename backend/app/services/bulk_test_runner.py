import json
from datetime import datetime

from app.services.llm import run_llm
from app.services.data_loader import load_locations, load_tags
from app.services.test_runner import run_all_validations, save_test_result


def run_bulk_tests():
    dataset = {
        "locations": load_locations(),
        "tags": load_tags()
    }

    with open("app/tests/test_cases.json", "r", encoding="utf-8") as f:
        questions = json.load(f)

    results = []
    scores = []

    for q in questions:
        answer = run_llm(q)

        final_score, detail = run_all_validations(
            q, answer, dataset
        )

        results.append({
            "question": q,
            "answer": answer,
            "score": final_score,
            "details": detail
        })

        scores.append(final_score)

    summary = {
        "average_score": sum(scores) / len(scores),
        "min_score": min(scores),
        "max_score": max(scores),
        "test_count": len(scores),
    }

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_path = f"app/test_results/BULK_{timestamp}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({
            "summary": summary,
            "results": results,
            "timestamp": timestamp
        }, f, indent=2, ensure_ascii=False)

    return summary, results, output_path
