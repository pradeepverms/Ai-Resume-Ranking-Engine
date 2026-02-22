# AI Resume Ranking & Hiring Simulation Engine

An end-to-end, explainable AI system that evaluates resume–job fit, explains scoring decisions, and simulates how specific improvements impact hiring outcomes.

This project is designed to **mimic real-world hiring logic**, not just demonstrate machine learning algorithms.

---

## 🚨 Problem Statement

Recruiters face three major problems during resume screening:

1. **Too many resumes, too little time**
2. **Keyword-based ATS systems miss real skill relevance**
3. **Candidates don’t know *why* they are rejected or *how* to improve**

Most student projects stop at resume parsing or basic ML scoring.  
This system goes further by acting as a **decision-support engine for hiring**.

---

## 🧠 Solution Overview

This project simulates how a recruiter or ATS system evaluates candidates by combining:

- Skill matching
- Project relevance
- Experience weighting
- Transformer-based semantic understanding
- Explainable scoring logic
- What-if career improvement simulation

Instead of only producing a score, the system answers:
> *Why did this resume score low, and what exact improvement would increase the chances?*

---

## 🏗️ System Architecture (High Level)

Resume Data ─┐ ├─▶️ Scoring Engine ─▶️ Final Score Job Data ────┘          │ ├─ Skill Match ├─ Project Relevance ├─ Experience Weight └─ Semantic Similarity (Sentence-BERT)
Final Score ─▶️ Explainability Engine ─▶️ What-If Simulator ─▶️ JD Sensitivity Analyzer
---

## ✨ Key Features
## Ethical AI & Bias Awareness
The system includes JD sensitivity analysis to detect:
- Over-weighted requirements
- Unrealistic skill expectations
- Minor wording changes causing major rank shifts

This helps prevent biased or unstable hiring decisions.
### 1️⃣ Resume–Job Ranking
Scores a resume against a job description using weighted evaluation.

**Endpoint**

POST /rank/job/{job_id}/resume/{resume_id}
**Output**
- Final score
- Component-wise score breakdown
- Human-readable explanation

---

### 2️⃣ Explainable Scoring (XAI)
Each score is broken into interpretable components:
- Skill match
- Project relevance
- Experience
- Semantic similarity

This avoids black-box ML decisions.

---

### 3️⃣ What-If Career Simulator 🔥
Simulates how adding a skill or experience would change the resume score.

**Example**
POST /simulate/job/1/resume/1?improvement=FastAPI
**Output**
```json
{
  "current_score": 23.86,
  "simulated_score": 43.19,
  "delta": 19.33
}
This helps candidates make data-driven career decisions.
4️⃣ JD Sensitivity Analysis
Evaluates how the same resume performs across multiple job roles.
POST /sensitivity/resume/{resume_id}
Use case
Identifies best-fit roles
Shows role alignment mismatch
Helps candidates target the right jobs
5️⃣ Multi-Resume Ranking
Ranks multiple resumes for a single job, similar to an ATS shortlist.
Endpoint
POST /rank/job/{job_id}/all-resumes
🧠 Machine Learning & NLP Techniques Used
Sentence-BERT (all-MiniLM-L6-v2) for semantic similarity
Cosine similarity on transformer embeddings
Rule-based + weighted scoring logic
Explainable AI principles (XAI)
This hybrid approach balances accuracy, interpretability, and performance.
🛠️ Tech Stack
Python
FastAPI
Sentence-Transformers (HuggingFace)
Scikit-learn
Uvicorn
🚀 How to Run Locally
1️⃣ Install dependencies
pip install fastapi uvicorn sentence-transformers torch scikit-learn
2️⃣ Start server
uvicorn main:app --reload
3️⃣ Open API docs
http://127.0.0.1:8000/docs
🔮 Future Improvements
Resume and JD embeddings stored in vector databases
PostgreSQL / SQLite integration
Authentication for recruiters vs candidates
Streamlit / React frontend
Dockerized deployment
👨‍💻 Author
Pradip Kumar Verma
B.Tech – Artificial Intelligence & Data Science
Focused on building real-world AI systems, not just academic models.