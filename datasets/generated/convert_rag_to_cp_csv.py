import json
import pandas as pd

# Load all JSON files
with open("norms_japan.json", "r", encoding="utf-8") as f:
    norms = json.load(f)

with open("scenarios_japan.json", "r", encoding="utf-8") as f:
    scenarios = json.load(f)

with open("questions_japan.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

with open("answers_japan.json", "r", encoding="utf-8") as f:
    answers = json.load(f)

# Build a structure for quick access
scenario_map = {s["id"]: s["text"] for s in scenarios["scenarios"]}

# Group answers by question_id
answer_groups = {}
for a in answers["answers"]:
    qid = a["question_id"]
    answer_groups.setdefault(qid, []).append(a["text"])

# Ensure each question has exactly 5 options
for k in answer_groups:
    answer_groups[k] = answer_groups[k][:5]

rows = []

for q in questions["questions"]:
    qid = q["id"]
    trait = q["trait"][0].upper()  # e.g. Openness -> O

    # FIXED COLUMN ORDER ↓↓↓
    row = {
        "scenario_text": q["scenario_text"],
        "question": q["text"],

        # Correct order expected by test_setup()
        "moderately_high": answer_groups[qid][1],
        "low": answer_groups[qid][4],
        "high": answer_groups[qid][0],
        "medium": answer_groups[qid][2],
        "moderately_low": answer_groups[qid][3],

        "trait": trait
    }
    rows.append(row)

df = pd.DataFrame(rows)

# IMPORTANT: Ensure answers with commas are quoted properly
df.to_csv("cp_questions_japan.csv", index=False, encoding="utf-8-sig", quoting=1)

print("DONE! Saved cp_questions_japan.csv")
