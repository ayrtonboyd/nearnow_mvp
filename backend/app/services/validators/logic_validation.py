def validate(question: str, answer: str, dataset):
    notes = []
    score = 10

    # Extract venue names
    from .venue_extraction import extract_venue_names
    venues = extract_venue_names(answer)

    # Build lookup table
    name_to_data = {loc["name"]: loc for loc in dataset["locations"]}

    # Infer type from question
    desired_type = None
    if "cafe" in question.lower() or "café" in question.lower():
        desired_type = "Café"
    if "pub" in question.lower():
        desired_type = "Pub"

    for v in venues:
        if v not in name_to_data:
            continue
        
        data = name_to_data[v]

        # Type mismatch
        if desired_type and data["type"] != desired_type:
            score -= 3
            notes.append(f"Venue '{v}' does not match requested type '{desired_type}'.")

        # Tag checks
        for tag in ["cosy", "lively", "vegan", "dog-friendly", "wifi", "outdoor seating"]:
            if tag in question.lower() and not any(tag.lower() in t.lower() for t in data["tags"]):
                score -= 2
                notes.append(f"Venue '{v}' missing required tag: {tag}.")

    return max(score, 0), notes
