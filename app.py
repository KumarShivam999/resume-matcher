import streamlit as st
import requests
import pdfplumber

st.title("Resume Matcher")
st.write("Upload your resume and paste the job description to see your match score and skill gaps.")

def extract_text_from_pdf(uploaded_file):
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
jd_text = st.text_area("Paste the job description here", height=200)

if st.button("Analyze"):
    if resume_file and jd_text:
        resume_text = extract_text_from_pdf(resume_file)

        if not resume_text.strip():
            st.error("Couldn't extract text from this PDF. Try a different file.")
        else:
            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                json={"resume_text": resume_text, "jd_text": jd_text}
            )
            result = response.json()

            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("TF-IDF Score", f"{result['tfidf_score']}%")
            with col_b:
                st.metric("Semantic Score", f"{result['semantic_score']}%")

            col1, col2 = st.columns(2)
            with col1:
                st.write("✅ Matched Skills")
                st.write(result['matched_skills'])
            with col2:
                st.write("❌ Missing Skills")
                st.write(result['missing_skills'])
    else:
        st.warning("Please upload a resume PDF and paste the job description.")