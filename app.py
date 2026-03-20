from flask import Flask, render_template, request, jsonify
from utils.parser import extract_text
from utils.analyzer import analyze_resume
from utils.interviewer import generate_questions
from utils.evaluator import evaluate_answer

app = Flask(__name__)

resume_text_global = ""
questions_global = []


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    global resume_text_global, questions_global

    try:
        file = request.files['resume']
        resume_text_global = extract_text(file)

        print("Resume length:", len(resume_text_global))

        if not resume_text_global.strip():
            return jsonify({
                "analysis": {
                    "resume_skills": [],
                    "jd_skills": [],
                    "matched_skills": [],
                    "missing_skills": [],
                    "recommendations": [],
                    "score": 0,
                    "semantic_score": 0
                },
                "questions": ["⚠️ Upload a valid resume"]
            })

        jd = request.form.get('jd', '')
        analysis = analyze_resume(resume_text_global, jd)

        # ✅ FIX: pass text not list
        questions_global = generate_questions(resume_text_global)

        return jsonify({
            "analysis": analysis,
            "questions": questions_global
        })

    except Exception as e:
        print("🔥 ERROR:", e)
        return jsonify({"error": str(e)}), 500


@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json

    question = data.get('question', '')
    answer = data.get('answer', '')

    result = evaluate_answer(answer, question)

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)