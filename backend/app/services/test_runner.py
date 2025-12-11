import json
from datetime import datetime

from app.services.validators.length_validation import validate as length_validate
from app.services.validators.tone_validation import validate as tone_validate
from app.services.validators.structure_validation import validate as structure_validate
from app.services.validators.style_validation import validate as style_validate
from app.services.validators.logic_validation import validate as logic_validate

VALIDATORS = {
    "length": length_validate,
    "tone": tone_validate,
    "structure": structure_validate,
    "style": style_validate,
    "logic": logic_validate,
}


def run_all_validations(question: str, answer: str, dataset: dict):
    results = {}
    total_score = 0

    for name, validator in VALIDATORS.items():
        score, notes = validator(question, answer, dataset)
        results[name] = {
            "score": score,
            "notes": notes
        }
        total_score += score

    final_score = total_score / len(VALIDATORS)

    return final_score, results


def save_test_result(question: str, answer: str, final_score: float, results: dict):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_path = f"app/test_results/{timestamp}.json"

    data = {
        "timestamp": timestamp,
        "question": question,
        "answer": answer,
        "final_score": final_score,
        "details": results,
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return output_path
