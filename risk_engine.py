# risk_engine.py
# Simple, explicit ATS risk rules

def analyze_risk(resume, skill_match_percent: float) -> int:
    """
    Lower is better.
    0 = no risk
    """

    risk = 0

    # Low skill match = risk
    if skill_match_percent < 40:
        risk += 2

    # Very low experience = risk
    if resume.experience_years < 1:
        risk += 1

    # Empty resume text = big risk
    if not resume.resume_text or len(resume.resume_text.strip()) < 50:
        risk += 2

    return risk