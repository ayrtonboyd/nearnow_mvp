def validate(question: str, answer: str, dataset=None):
    notes = []
    score = 10

    words = len(answer.split())
    if words > 120:
        score -= 5
        notes.append(f"Response too long: {words} words (limit ~120).")

    # Opening line limit
    first_line = answer.split("\n")[0]
    if len(first_line.split()) > 20:
        score -= 2
        notes.append("Opening line exceeds 20 words.")

    # Closing line limit
    last_line = answer.strip().split("\n")[-1]
    if len(last_line.split()) > 10:
        score -= 2
        notes.append("Closing line exceeds 10 words.")

    return score, notes
