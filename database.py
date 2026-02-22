# database.py

JOBS = {
    1: {
        "id": 1,
        "required_skills": ["Python", "SQL", "FastAPI"],
        "raw_text": "Looking for Python backend intern with SQL and FastAPI experience"
    },
    2: {
        "id": 2,
        "required_skills": ["Machine Learning", "Pandas", "NumPy"],
        "raw_text": "Hiring ML intern with strong Python, Pandas and NumPy skills"
    },
    3: {
        "id": 3,
        "required_skills": ["Python", "Deep Learning"],
        "raw_text": "AI intern role focused on deep learning and Python"
    }
}

# ---------------- MOCK RESUME DATA ---------------- #

RESUMES = {
    1: {
        "id": 1,
        "skills": ["Python", "Pandas"],
        "projects": [
            {
                "title": "Loan Approval System",
                "tech": ["Python", "Sklearn"]
            }
        ],
        "experience_years": 0,
        "raw_text": "B.Tech AI student with Python and ML projects"
    },
    2: {
        "id": 2,
        "skills": ["Python", "SQL", "FastAPI"],
        "projects": [
            {
                "title": "Resume Ranker",
                "tech": ["Python", "FastAPI"]
            }
        ],
        "experience_years": 1,
        "raw_text": "Backend focused student with FastAPI and SQL experience"
    }
}

# ---------------- ACCESS FUNCTIONS ---------------- #

def get_job_by_id(job_id: int):
    return JOBS.get(job_id)


def get_all_jobs():
    return list(JOBS.values())


def get_resume_by_id(resume_id: int):
    return RESUMES.get(resume_id)


def get_all_resumes():
    return list(RESUMES.values())