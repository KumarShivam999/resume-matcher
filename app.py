import streamlit as st
import requests

st.title("Resume Matcher")
st.write("Paste your resume and a job description to see your match score and skill gaps.")

resume_text = st.text_area("Paste your resume text here", height=200)
jd_text = st.text_area("Paste the job description here", height=200)

if st.button("Analyze"):
    if resume_text and jd_text:
        response = requests.post(
            "http://127.0.0.1:8000/analyze",
            json={"resume_text": resume_text, "jd_text": jd_text}
        )
        result = response.json()

        st.subheader(f"Match Score: {result['match_score']}%")

        col1, col2 = st.columns(2)
        with col1:
            st.write("✅ Matched Skills")
            st.write(result['matched_skills'])
        with col2:
            st.write("❌ Missing Skills")
            st.write(result['missing_skills'])
    else:
        st.warning("Please paste both resume and job description text.")