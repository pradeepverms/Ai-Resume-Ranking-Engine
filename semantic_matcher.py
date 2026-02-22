# semantic_matcher.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Lightweight but powerful model
model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_similarity_score(resume_text: str, job_text: str) -> float:
    """
    Uses Sentence-BERT embeddings to compute semantic similarity
    Returns value between 0.0 and 1.0
    """

    if not resume_text or not job_text:
        return 0.0

    embeddings = model.encode([resume_text, job_text])
    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return round(float(similarity), 3)