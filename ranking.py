# ranking.py

from semantic_matcher import semantic_similarity_score

WEIGHTS = {
    "skill": 0.35,
    "project": 0.25,
    "experience": 0.15,
    "semantic": 0.25
}


def calculate_score(resume, job, return_breakdown=False):

    skill_score = skill_match(resume, job)
    project_score = project_match(resume, job)
    experience_score = experience_score_fn(resume)
    semantic_score = semantic_similarity_score(
        resume.get("raw_text", ""),
        job.get("raw_text", "")
    )

    weighted = {
        "skill_match": WEIGHTS["skill"] * skill_score * 100,
        "project_relevance": WEIGHTS["project"] * project_score * 100,
        "experience": WEIGHTS["experience"] * experience_score * 100,
        "semantic_match": WEIGHTS["semantic"] * semantic_score * 100
    }

    final_score = round(sum(weighted.values()), 2)

    if return_breakdown:
        return final_score, weighted

    return final_score


# ---------------- HELPERS ---------------- #

def skill_match(resume, job):
    r = set(resume.get("skills", []))
    j = set(job.get("required_skills", []))
    return len(r & j) / len(j) if j else 0.0


def project_match(resume, job):
    score = 0
    for p in resume.get("projects", []):
        for tech in p.get("tech", []):
            if tech in job.get("required_skills", []):
                score += 1
    return min(score / 5, 1.0)


def experience_score_fn(resume):
    y = resume.get("experience_years", 0)
    if y >= 2:
        return 1.0
    if y == 1:
        return 0.6
    return 0.2