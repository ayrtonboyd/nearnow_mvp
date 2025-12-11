import csv
import json
from pathlib import Path

# ---------- CONFIG ----------
locations_csv = Path("app/data/locations.csv")
tags_csv = Path("app/data/tags.csv")

locations_json = Path("app/data/locations.json")
tags_json = Path("app/data/tags.json")
# ----------------------------

# Convert locations
locations = []
with locations_csv.open() as f:
    reader = csv.DictReader(f)
    for row in reader:
        tags = [row["Tag1"], row["Tag2"], row["Tag3"]]
        tags = [t for t in tags if t]  # remove empty ones

        locations.append({
            "name": row["Name"].strip(),
            "type": row["Type"].strip(),
            "opening_hours": row["Opening Hours"].strip(),
            "description": row["Description"].strip(),
            "tags": tags
        })

with locations_json.open("w") as f:
    json.dump(locations, f, indent=2, ensure_ascii=False)


# Convert tags
tags = []
with tags_csv.open() as f:
    reader = csv.DictReader(f)
    for row in reader:
        tags.append({
            "category": row["Category"].strip(),
            "tag": row["Tag"].strip(),
            "description": row["Description"].strip(),
            "example": row["Example Use"].strip()
        })

with tags_json.open("w") as f:
    json.dump(tags, f, indent=2, ensure_ascii=False)

print("Conversion complete!")
