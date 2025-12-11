def validate(question: str, answer: str, dataset=None):
    notes = []
    score = 10

    lines = [l.strip() for l in answer.split("\n") if l.strip()]

    # Must have at least 3–4 lines: opener, venues, closer
    if len(lines) < 4:
        notes.append("Response structure too short or missing sections.")
        score -= 3

    # Opening line check
    if not any(phrase in lines[0].lower() for phrase in ["i know", "that sounds", "great choice", "lovely idea"]):
        notes.append("Opening line does not follow conversational pattern.")
        score -= 2

    # Closing line check
    last_line = lines[-1].lower()
    closers = [
        "which one sounds best to you",
        "want a few more ideas",
        "fancy another option",
        "any of these take your eye",
        "would you like me to narrow it down",
        "do you want me to find more like these"
    ]

    if not any(c in last_line for c in closers):
        notes.append("Closing line not from allowed variations.")
        score -= 2

    return max(score, 0), notes
