from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 🔥 Skills with variations
SKILLS = {
    "python": ["python"],
    "java": ["java"],
    "machine learning": ["machine learning", "ml", "model training"],
    "javascript": ["javascript", "js", "web", "frontend"],
    "sql": ["sql", "database"],
    "html": ["html", "web development"],
    "css": ["css", "styling"],
    "react": ["react", "reactjs"],
    "flask": ["flask"],
    "django": ["django"]
}


# 🔥 Semantic similarity
def semantic_match(resume, jd):
    try:
        if not resume.strip() or not jd.strip():
            return 0

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume, jd])
        similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

        return int(similarity * 100)

    except:
        return 0


# 🔍 Skill extraction
def extract_skills(text):
    if not text:
        return []

    text = text.lower()
    found = []

    for skill, variations in SKILLS.items():
        for v in variations:
            if v in text:
                found.append(skill)
                break

    return list(set(found))


# 🧠 Main analyzer
def analyze_resume(resume_text, jd_text=None):

    # 🔥 safety check
    if not resume_text or not resume_text.strip():
        return {
            "resume_skills": [],
            "jd_skills": [],
            "matched_skills": [],
            "missing_skills": [],
            "recommendations": [],
            "score": 0,
            "semantic_score": 0
        }

    resume_skills = extract_skills(resume_text)

    # 🔥 If JD provided
    if jd_text and jd_text.strip():

        jd_skills = extract_skills(jd_text)

        if len(jd_skills) == 0:
            matched = []
            skill_score = 0
        else:
            matched = [s for s in resume_skills if s in jd_skills]
            skill_score = int((len(matched) / len(jd_skills)) * 100)

        missing = [s for s in jd_skills if s not in resume_skills]
        recommendations = missing

        semantic_score = semantic_match(resume_text, jd_text)

        combined_score = int((skill_score * 0.6) + (semantic_score * 0.4))

        return {
            "resume_skills": resume_skills,
            "jd_skills": jd_skills,
            "matched_skills": matched,
            "missing_skills": missing,
            "recommendations": recommendations,
            "score": combined_score,
            "semantic_score": semantic_score
        }

    # 🔹 If NO JD → basic score
    basic_score = int((len(resume_skills) / len(SKILLS)) * 100)

    return {
        "resume_skills": resume_skills,
        "jd_skills": [],
        "matched_skills": [],
        "missing_skills": [],
        "recommendations": [],
        "score": basic_score,
        "semantic_score": 0
    }


# 🔥 Optional job match
def match_job(resume, jd):
    return semantic_match(resume, jd)