FORBIDDEN = [
    "Here are",
    "There are only",
    "Only one option",
    "Just one option",
    "According to the dataset",
    "Dataset",
    "Based on tags",
]

APOLOGETIC = [
    "only one that fits",
    "just two available",
    "sorry",
    "unfortunately",
]

def validate(question: str, answer: str, dataset=None):
    notes = []
    score = 10

    lower = answer.lower()

    # Check forbidden robotic language
    for phrase in FORBIDDEN:
        if phrase.lower() in lower:
            notes.append(f"Robotic phrase used: '{phrase}'")
            score -= 3

    # Check apologetic tone
    for phrase in APOLOGETIC:
        if phrase in lower:
            notes.append(f"Apologetic phrasing detected: '{phrase}'")
            score -= 2

    # Check warmth (simple heuristic)
    if "I know" not in answer and "you might like" not in answer:
        notes.append("Opening lacks warmth indicators.")
        score -= 1

    return max(score, 0), notes
