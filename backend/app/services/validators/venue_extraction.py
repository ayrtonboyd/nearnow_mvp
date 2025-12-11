import re

def extract_venue_names(answer: str):
    """
    Looks for lines formatted like:
    **Farmhouse Kitchen**
    """
    pattern = r"\*\*(.+?)\*\*"
    return re.findall(pattern, answer)


def validate(question: str, answer: str, dataset):
    notes = []
    score = 10

    # Extract venues from markdown bold headings
    venues = extract_venue_names(answer)

    if len(venues) == 0:
        score -= 5
        notes.append("No venue names detected.")

    if len(venues) < 2:
        notes.append("Fewer than 2 venues detected.")
        score -= 2

    if len(venues) > 3:
        notes.append("More than 3 venues detected.")
        score -= 2

    # Check dataset presence
    dataset_names = {loc["name"] for loc in dataset["locations"]}

    for v in venues:
        if v not in dataset_names:
            notes.append(f"Venue '{v}' not found in dataset.")
            score -= 3

    return max(score, 0), notes
