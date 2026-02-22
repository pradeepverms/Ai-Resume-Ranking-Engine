# resume_rewriter.py

import re

ACTION_VERBS = [
    "Developed", "Designed", "Implemented", "Built",
    "Optimized", "Integrated", "Created", "Maintained"
]

def extract_keywords(text: str):
    text = text.lower()
    words = re.findall(r"[a-zA-Z+#.]+", text)
    stopwords = {
        "and","or","the","with","using","for","to","of","in","on","a","an"
    }
    return set(w for w in words if w not in stopwords and len(w) > 2)


def rewrite_resume(resume_text: str, resume_skills: str, job_description: str):
    resume_kw = extract_keywords(resume_text)
    job_kw = extract_keywords(job_description)

    common_keywords = resume_kw.intersection(job_kw)

    bullets = []
    verb_index = 0

    for skill in resume_skills.split(","):
        skill = skill.strip().lower()
        if not skill:
            continue

        related = [kw for kw in common_keywords if skill in kw or kw in skill]
        if not related:
            continue

        verb = ACTION_VERBS[verb_index % len(ACTION_VERBS)]
        verb_index += 1

        bullet = (
            f"{verb} backend components using {skill} "
            f"aligned with job requirements"
        )
        bullets.append(bullet)

    # fallback (resume empty nahi rehna chahiye)
    if not bullets:
        bullets.append(
            "Worked on backend development tasks relevant to the job role"
        )

    return {
        "rewritten_bullets": bullets,
        "used_keywords": sorted(common_keywords)
    }