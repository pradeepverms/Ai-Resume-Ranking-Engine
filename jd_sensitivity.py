# jd_sensitivity.py

from ranking import calculate_score


def analyze_jd_sensitivity(resume, jobs: list):

    results = []

    for job in jobs:
        score = calculate_score(resume, job)
        results.append({
            "job_id": job["id"],
            "score": score
        })

    best_job = max(results, key=lambda x: x["score"])

    return {
        "job_scores": results,
        "best_fit_job": best_job["job_id"],
        "best_score": best_job["score"]
    }