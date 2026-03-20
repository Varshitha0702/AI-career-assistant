def generate_questions(text):
    text = text.lower()
    questions = []

    if "python" in text:
        questions.append("Explain Python OOP concepts.")

    if "machine learning" in text or "ml" in text:
        questions.append("What is overfitting?")

    if "sql" in text:
        questions.append("What is JOIN in SQL?")

    questions.append("Tell me about yourself.")

    return questions