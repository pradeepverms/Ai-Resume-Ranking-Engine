def extract_required_skills(text: str):
    text = text.lower()

    MUST_HAVE = [
        "python", "sql", "fastapi"
    ]

    GOOD_TO_HAVE = [
        "machine learning", "docker", "aws"
    ]

    must = [s for s in MUST_HAVE if s in text]
    good = [s for s in GOOD_TO_HAVE if s in text]

    return {
        "must_have": must,
        "good_to_have": good
    }