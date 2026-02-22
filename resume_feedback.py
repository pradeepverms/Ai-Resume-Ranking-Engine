# resume_feedback.py

def generate_feedback(resume: dict, job: dict, semantic_similarity: float) -> dict:
    """
    Resume feedback engine for ATS.
    Returns missing skills, weak areas, suggested keywords and tips.
    ALWAYS returns a dict.
    """

    resume_skills = set([s.lower() for s in resume.get("skills", [])])
    job_skills = set([s.lower() for s in job.get("skills", [])])

    missing_skills = list(job_skills - resume_skills)
    matched_skills = list(job_skills & resume_skills)

    weak_areas = []
    if semantic_similarity < 0.5:
        weak_areas.append("Resume content is weakly aligned with job context")

    suggestions = matched_skills + missing_skills

    tips = []
    if missing_skills:
        tips.append("Add missing job-relevant skills explicitly")
    if semantic_similarity < 0.6:
        tips.append("Rewrite experience using job description language")
    if not tips:
        tips.append("Resume is well aligned, focus on quantified impact")

    return {
        "missing_skills": missing_skills,
        "weak_areas": weak_areas,
        "suggested_keywords": suggestions,
        "resume_tips": tips
    }