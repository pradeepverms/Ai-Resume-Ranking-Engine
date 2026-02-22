# Design Decisions – AI Resume Ranking Engine

## Why this project exists
Most resume screeners rely on keyword matching or raw cosine similarity.
This fails in real hiring because:
- It ignores skill gaps
- It cannot explain decisions
- It breaks under slight wording changes

This system is designed to simulate **how a human recruiter thinks**, not how a script matches text.

---

## Why Sentence Transformers (not TF-IDF)
TF-IDF fails on semantic similarity.
Sentence Transformers capture meaning, context, and transferable skills.

This allows:
- “Data Analysis” ≈ “Exploratory Data Analysis”
- “ML Engineer” ≈ “Applied Machine Learning”

---

## Why Hybrid Scoring (Rules + ML)
Pure ML scores are fragile.
Pure rules are rigid.

I intentionally use:
- ML for semantic similarity
- Rules for penalties (gaps, missing core skills)
- Risk engine for hiring uncertainty

This mirrors **real hiring trade-offs**.

---

## Why Explainability is non-negotiable
Hiring systems without explanations are:
- Unfair
- Untrustworthy
- Legally risky

This project outputs:
- Skill gaps
- Score breakdown
- Sensitivity analysis

This is critical for ethical AI hiring.

---

## Known Trade-offs
- SQLite used instead of Postgres for simplicity
- No UI yet (API-first design)
- Latency not optimized yet

These are conscious decisions, not limitations.

---

## Future Direction
- Bias & fairness audits
- Vector databases (FAISS / pgvector)
- Recruiter vs Candidate role separation