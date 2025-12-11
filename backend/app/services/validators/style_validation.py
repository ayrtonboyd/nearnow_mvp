def validate(question: str, answer: str, dataset=None):
    notes = []
    score = 10

    # Check for unnatural tag listing
    if "Tags:" in answer:
        notes.append("Tag listing detected.")
        score -= 3

    # Check for friendly connectors
    connectors = ["so", "which makes it", "great for", "nicely", "you’ll like"]
    if not any(c in answer.lower() for c in connectors):
        notes.append("Missing friendly connective phrasing.")
        score -= 1

    return max(score, 0), notes
