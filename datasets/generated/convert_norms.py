import json
import pandas as pd

# Load the JSON norms file
with open("norms_japan.json", "r", encoding="utf-8") as f:
    data = json.load(f)

rows = []
for n in data["norms"]:
    rows.append({
        "country": data["country"],
        "norm": n["text"]
    })

df = pd.DataFrame(rows)
df.to_csv("country_norms.csv", index=False, encoding="utf-8-sig")

print("Saved country_norms.csv successfully!")
