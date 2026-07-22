import os
from dotenv import load_dotenv
from openai import OpenAI
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util

load_dotenv() 

SKILLS_LIST = [
    "python", "java", "javascript", "c++", "c",
    "sql", "postgresql", "mysql", "scikit-learn", "xgboost",
    "lightgbm", "power bi", "excel", "power query", "fastapi",
    "flask", "react", "node.js", "spacy", "nlp", "hdfs",
    "pandas", "numpy", "streamlit", "dax", "machine learning",
    "deep learning", "oop", "dbms", "os", "cn"
]

model = SentenceTransformer('all-MiniLM-L6-v2')

groq_client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def extract_skills(text):
    text_lower = text.lower()
    return set(skill for skill in SKILLS_LIST if skill in text_lower)

def get_tfidf_score(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(float(score) * 100, 2)

def get_semantic_score(resume_text, jd_text):
    embeddings = model.encode([resume_text, jd_text], convert_to_tensor=True)
    score = util.cos_sim(embeddings[0], embeddings[1]).item()
    return round(score * 100, 2)

def get_ai_feedback(resume_text, jd_text, missing_skills):
    prompt = f"""You are a senior recruiter reviewing a resume against a job description.

Job Description:
{jd_text}

Resume:
{resume_text}

Missing skills detected: {', '.join(missing_skills)}

Give a short, honest, 3-4 sentence assessment of this candidate's fit for the role, and one specific actionable suggestion to improve their resume. Be direct and professional."""

    response = groq_client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def analyze(resume_text, jd_text):
    tfidf_score = get_tfidf_score(resume_text, jd_text)
    semantic_score = get_semantic_score(resume_text, jd_text)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    matched = resume_skills & jd_skills
    missing = jd_skills - resume_skills

    ai_feedback = get_ai_feedback(resume_text, jd_text, list(missing))

    return {
        "tfidf_score": tfidf_score,
        "semantic_score": semantic_score,
        "matched_skills": list(matched),
        "missing_skills": list(missing),
        "jd_skills": list(jd_skills),
        "resume_skills": list(resume_skills),
        "ai_feedback": ai_feedback
    }

if __name__ == "__main__":
    with open("resume.txt", "r", encoding="utf-8") as f:
        resume_text = f.read()
    with open("jd.txt", "r", encoding="utf-8") as f:
        jd_text = f.read()

    result = analyze(resume_text, jd_text)
    print(result)