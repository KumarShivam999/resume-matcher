from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read both files
with open("resume.txt", "r", encoding="utf-8") as f:
    resume_text = f.read()

with open("jd.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()

# Convert text to TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words="english")
vectors = vectorizer.fit_transform([resume_text, jd_text])

# Compute similarity score
score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

print(f"Match Score: {score * 100:.2f}%")