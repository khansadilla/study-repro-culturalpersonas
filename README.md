# CulturalPersonas — MCS Reproduction

This repository contains a **reproduction study** of the *CulturalPersonas* benchmark,
focusing **only on the Multiple Choice Selection (MCS)** evaluation setting.

This work reproduces the original MCS experiment pipeline to analyze
LLM personality expression across different cultural contexts.

---

## Original Work

This project is based on the original **CulturalPersonas** benchmark:
https://github.com/limenlp/CulturalPersonas

All credits for dataset design and methodology belong to the original authors.

---

## Scope

- Evaluation setting: **Multiple Choice Selection (MCS)**
- Personality analysis using distribution-based metrics
- Models and configurations follow the original implementation unless stated otherwise

---

## Running MCS Experiments

```bash
cd experiments

python mcs.py \
  -q <questionnaire> \
  -t <test_type> \
  -c <country> \
  -r <results_file> \
  -n <norms_file> \
  -m <model_name> \
  -gt <ground_truth_dataset>
