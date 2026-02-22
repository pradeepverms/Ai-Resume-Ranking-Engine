# decision_engine.py
def decide(final_score: float) -> str:
    if final_score >= 75:
        return "STRONG_SHORTLIST"
    elif final_score >= 60:
        return "SHORTLIST"
    elif final_score >= 45:
        return "BORDERLINE"
    else:
        return "REJECT"


def explain(result: dict) -> str:
    reasons = []

    if result["skill_match_percent"] < 50:
        reasons.append("Low skill match")

    if result["semantic_score"] < 0.4:
        reasons.append("Weak contextual relevance")

    if result["experience_score"] == 0:
        reasons.append("Insufficient experience")

    if result["risk_score"] >= 3:
        reasons.append("Resume risk flags detected")

    if not reasons:
        return "Profile aligns well with job requirements"

    return ", ".join(reasons)