import spacy

# Load the small English model
nlp = spacy.load("en_core_web_sm")

# A manual skill list — this is common practice in resume-matching tools
# since spaCy alone doesn't know "XGBoost" or "FastAPI" are tech skills
SKILLS_LIST = [
    "python", "java", "javascript", "c++", "c",
    "sql", "postgresql", "mysql", "scikit-learn", "xgboost",
    "lightgbm", "power bi", "excel", "power query", "fastapi",
    "flask", "react", "node.js", "spacy", "nlp", "hdfs",
    "pandas", "numpy", "streamlit", "dax", "machine learning",
    "deep learning", "oop", "dbms", "os", "cn"
]

def extract_skills(text):
    text_lower = text.lower()
    found = set()
    for skill in SKILLS_LIST:
        if skill in text_lower:
            found.add(skill)
    return found

# Read both files
with open("resume.txt", "r", encoding="utf-8") as f:
    resume_text = f.read()

with open("jd.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()

resume_skills = extract_skills(resume_text)
jd_skills = extract_skills(jd_text)

matched_skills = resume_skills & jd_skills
missing_skills = jd_skills - resume_skills

print("Skills in JD:", jd_skills)
print()
print("Skills in your resume:", resume_skills)
print()
print("✅ Matched skills:", matched_skills)
print()
print("❌ Missing skills (add these!):", missing_skills)