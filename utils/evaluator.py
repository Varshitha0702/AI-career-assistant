def evaluate_answer(answer, question):
    answer = answer.lower()

    if len(answer.split()) < 5:
        return {"score": 10, "feedback": "Answer too short"}

    keyword_sets = {
        "overfitting": ["overfitting", "training", "test", "model"],
        "python": ["class", "object", "inheritance"],
        "sql": ["join", "table", "query"]
    }

    score = 0
    total_keywords = 0

    for key, words in keyword_sets.items():
        total_keywords += len(words)
        score += sum(1 for w in words if w in answer)

    score = int((score / total_keywords) * 100)

    if score < 40:
        feedback = "Basic answer"
    elif score < 70:
        feedback = "Good but can improve"
    else:
        feedback = "Strong answer"

    return {"score": score, "feedback": feedback}