# what_if_simulator.py

from ranking import calculate_score


def simulate_improvement(resume, job, improvement: str):
    """
    improvement: skill name OR 'experience'
    """

    simulated_resume = resume.copy()

    if improvement == "experience":
        simulated_resume["experience_years"] = (
            resume.get("experience_years", 0) + 1
        )

    else:
        skills = set(resume.get("skills", []))
        skills.add(improvement)
        simulated_resume["skills"] = list(skills)

        # fake project boost
        simulated_resume.setdefault("projects", []).append(
            {
                "title": f"{improvement} Practice Project",
                "tech": [improvement]
            }
        )

    new_score = calculate_score(simulated_resume, job)

    return new_score