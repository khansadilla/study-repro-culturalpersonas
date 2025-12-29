import pandas as pd

answers_path   = "../datasets/cp/answers/all_japan_answers.csv"
questions_path = "../datasets/cp/questions/all_japan_questions.csv"
scenarios_path = "../datasets/cp/scenarios/all_japan_scenarios.csv"
out_path       = "../datasets/cp/answers/all_japan_mcs_ready.csv"

a = pd.read_csv(answers_path)
q = pd.read_csv(questions_path)
s = pd.read_csv(scenarios_path)

a.columns = [c.strip() for c in a.columns]
q.columns = [c.strip() for c in q.columns]
s.columns = [c.strip() for c in s.columns]


aq = a.merge(
    q[["question", "trait", "scenario_id"]],
    on="question",
    how="left",
    suffixes=("", "_q")
)

aq = aq.drop(columns=["trait"])
aq = aq.rename(columns={"trait_q": "trait"})

# --- merge scenario text ---
aqs = aq.merge(
    s[["norm_id", "scenario"]],
    left_on="scenario_id",
    right_on="norm_id",
    how="left"
)

aqs = aqs.rename(columns={"scenario": "scenario_text"})

# --- sanity check ---
need = [
    "scenario_text",
    "question",
    "trait",
    "high",
    "moderately_high",
    "medium",
    "moderately_low",
    "low"
]

missing = [c for c in need if c not in aqs.columns]
if missing:
    raise SystemExit(f"Missing columns: {missing}")

aqs[need].to_csv(out_path, index=False)
print("✅ WROTE:", out_path)
print("Rows:", len(aqs))
