import re

COMMON_SKILLS = [
    "python", "java", "c++", "sql", "mysql",
    "machine learning", "deep learning",
    "fastapi", "django", "flask",
    "pandas", "numpy", "scikit-learn",
    "data science", "ai"
]


def extract_skills(text: str):
    text = text.lower()
    found_skills = []

    for skill in COMMON_SKILLS:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


def extract_experience_years(text: str):
    """
    Examples it should catch:
    - 2 years experience
    - 3+ years
    - experience: 1 year
    """
    matches = re.findall(r"(\d+)\+?\s+years?", text.lower())

    if not matches:
        return 0

    return max(int(x) for x in matches)