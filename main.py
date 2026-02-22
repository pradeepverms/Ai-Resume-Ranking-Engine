# main.py

from fastapi import FastAPI, HTTPException

from database import (
    get_job_by_id,
    get_all_jobs,
    get_resume_by_id,
    get_all_resumes
)

from ranking import calculate_score
from explainbility import generate_explanation
from what_if_simulator import simulate_improvement
from jd_sensitivity import analyze_jd_sensitivity

app = FastAPI(title="AI Resume Ranking & Hiring Simulation Engine")


# ---------------- HEALTH ---------------- #

@app.get("/health")
def health():
    return {"status": "ok"}


# ---------------- SINGLE RESUME RANK ---------------- #

@app.post("/rank/job/{job_id}/resume/{resume_id}")
def rank_resume(job_id: int, resume_id: int):

    job = get_job_by_id(job_id)
    resume = get_resume_by_id(resume_id)

    if not job or not resume:
        raise HTTPException(status_code=404, detail="Job or Resume not found")

    score, breakdown = calculate_score(resume, job, return_breakdown=True)
    explanation = generate_explanation(resume, job, score)

    return {
        "final_score": score,
        "score_breakdown": breakdown,
        "explanation": explanation
    }


# ---------------- WHAT-IF SIMULATOR ---------------- #

@app.post("/simulate/job/{job_id}/resume/{resume_id}")
def simulate_resume_improvement(
    job_id: int,
    resume_id: int,
    improvement: str
):

    job = get_job_by_id(job_id)
    resume = get_resume_by_id(resume_id)

    if not job or not resume:
        raise HTTPException(status_code=404, detail="Job or Resume not found")

    current = calculate_score(resume, job)
    simulated = simulate_improvement(resume, job, improvement)

    return {
        "current_score": current,
        "simulated_score": simulated,
        "improvement": improvement,
        "delta": round(simulated - current, 2)
    }


# ---------------- JD SENSITIVITY ---------------- #

@app.post("/sensitivity/resume/{resume_id}")
def jd_sensitivity(resume_id: int):

    resume = get_resume_by_id(resume_id)
    jobs = get_all_jobs()

    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    return analyze_jd_sensitivity(resume, jobs)


# ---------------- MULTI-RESUME RANKING ---------------- #

@app.post("/rank/job/{job_id}/all-resumes")
def rank_all_resumes(job_id: int):

    job = get_job_by_id(job_id)
    resumes = get_all_resumes()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    ranked = []

    for resume in resumes:
        score = calculate_score(resume, job)
        ranked.append({
            "resume_id": resume["id"],
            "score": score
        })

    ranked.sort(key=lambda x: x["score"], reverse=True)

    return ranked