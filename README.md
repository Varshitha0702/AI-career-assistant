# 🚀 AI Career Assistant

An intelligent web-based system that analyzes resumes, performs ATS-based scoring, matches jobs, and generates interview questions to help users prepare effectively.

---

## 🌟 Features

* 📄 Resume Parsing (PDF)
* 🧠 Skill Extraction using NLP techniques
* 📊 ATS-Based Resume Scoring
* 🔍 Job Description Matching (TF-IDF + Cosine Similarity)
* 🎤 Automatic Interview Question Generation
* ✍️ Answer Evaluation with Feedback
* 💡 Skill Gap Analysis & Recommendations

---

## 🧠 Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn (TF-IDF, Cosine Similarity)
* **Frontend:** HTML, CSS, JavaScript
* **PDF Processing:** PyPDF2

---

## ⚙️ How It Works

1. Upload your resume (PDF)
2. Enter a Job Description
3. System extracts skills from resume
4. Compares with job requirements
5. Generates:

   * ATS Score
   * Matched & Missing Skills
   * Recommendations
6. Provides interview questions
7. Evaluates your answers with feedback

---

## 📊 Scoring Logic

* **Skill Matching:** 60%
* **Semantic Similarity (NLP):** 40%
* Uses TF-IDF + Cosine Similarity for intelligent matching

---

## 🚀 Run Locally

```bash
# Clone repository
git clone https://github.com/Varshitha0702/AI-career-assistant.git

# Navigate to folder
cd AI-career-assistant

# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate

# Install dependencies
pip install flask scikit-learn PyPDF2

# Run application
python app.py
```

---

## 📁 Project Structure

```
AI-career-assistant/
│
├── app.py
├── utils/
│   ├── analyzer.py
│   ├── parser.py
│   ├── interviewer.py
│   ├── evaluator.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## 🎯 Key Highlights

* Built an end-to-end career assistant system
* Implements NLP-based resume analysis
* Provides personalized interview preparation
* Handles real-world resume parsing challenges
* Designed with modular and scalable architecture

---

## 🧠 Future Improvements

* Add OCR support for scanned PDFs
* Improve NLP using advanced models
* Add user authentication
* Store history of analyses

---

## 👩‍💻 Author

**Varshitha Gudikandula**
🔗 GitHub: https://github.com/Varshitha0702

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
