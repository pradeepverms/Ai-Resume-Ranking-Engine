# explainability.py

def generate_explanation(resume, job, score):
    strong_points = []
    weak_points = []
    improvement_actions = []

    resume_skills = set(resume["skills"])
    job_skills = set(job["required_skills"])

    matched = resume_skills.intersection(job_skills)
    missing = job_skills - resume_skills

    if matched:
        strong_points.append(f"Matched key skills: {', '.join(list(matched)[:3])}")

    if missing:
        weak_points.append(f"Missing required skills: {', '.join(list(missing)[:3])}")
        for skill in list(missing)[:2]:
            improvement_actions.append(
                f"Learn/add project using {skill} (+6-10%)"
            )

    if not resume.get("projects"):
        weak_points.append("No strong technical projects")
        improvement_actions.append("Add 1 real-world project (+12%)")

    if resume.get("experience_years", 0) == 0:
        weak_points.append("No industry experience")
        improvement_actions.append("Do internship or freelancing (+8%)")

    return {
        "final_score": score,
        "strong_points": strong_points,
        "weak_points": weak_points,
        "improvement_actions": improvement_actions
    }