from utils.analyzer import extract_skills

test_cases = [
    ("Python SQL ML", ["python", "sql", "machine learning"]),
    ("HTML CSS JS", ["html", "css", "javascript"]),
]

correct = 0
total = 0

for text, expected in test_cases:
    result = extract_skills(text)

    for skill in expected:
        total += 1
        if skill in result:
            correct += 1

accuracy = (correct / total) * 100
print("Accuracy:", accuracy)