# gap_engine.py

def analyze_jd_gap(resume: dict, job: dict) -> dict:
    """
    Job Description Gap Analysis Engine
    Compares resume skills & experience vs job requirements
    ALWAYS returns a dict
    """

    resume_skills = set([s.lower() for s in resume.get("skills", [])])
    job_skills = set([s.lower() for s in job.get("skills", [])])

    missing_skills = list(job_skills - resume_skills)
    overqualified_skills = list(resume_skills - job_skills)

    weak_skills = []  # future use (experience depth etc.)

    required_exp = job.get("experience_years", 0)
    found_exp = resume.get("experience_years", 0)

    if found_exp >= required_exp:
        status = "MEETS"
    else:
        status = "BELOW"

    return {
        "missing_skills": missing_skills,
        "weak_skills": weak_skills,
        "overqualified_skills": overqualified_skills,
        "experience_gap": {
            "required": required_exp,
            "found": found_exp,
            "status": status
        }
    }