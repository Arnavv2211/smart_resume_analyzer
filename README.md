# 📄 Smart Resume Analyzer using NLP + Machine Learning

A web app that analyzes your resume against a job description using NLP and machine learning to calculate how well your resume matches the JD — and gives suggestions for improvement.

---

##  Features

-  Upload resume in PDF or DOCX format
-  Paste a job description directly
-  Intelligent text comparison using NLP (TF-IDF + cosine similarity)
-  Shows match score (0–100%)
-  Gives suggestions to improve resume relevance
-  Balloon animation for great matches!

---

##  Tech Stack

- **Frontend & UI:** Streamlit
- **Backend Logic:** Python
- **Text Processing:** NLTK, scikit-learn, re
- **Resume Parsing:** PyPDF2, docx2txt
- **Deployment:** Streamlit Cloud *(see below)*

---

##  How It Works

1. Upload your resume (PDF or DOCX)
2. Paste the job description
3. App cleans and preprocesses both texts
4. Applies TF-IDF vectorization
5. Uses cosine similarity to score the match
6. Shows you the match score + feedback

---

##  Installation (Local)

```bash
# Clone the repo
git clone https://github.com/Arnavv2211/smart_resume_analyzer.git
cd smart_resume_analyzer

# Create virtual environment
python -m venv venv
venv\Scripts\activate 

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---


## ✍ Author

**Arnav Mahajan**  
🔗 [GitHub](https://github.com/Arnavv2211)  
📧 arnavmaha2211@gmail.com 
🎓 Fresher Engineer | Python & ML Enthusiast

---

## 📌 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it with attribution.

