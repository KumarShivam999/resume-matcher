# Resume Matcher

An AI-powered tool that compares a resume against a job description, calculates a match score, and identifies missing skills — helping job seekers understand exactly where their resume falls short.

## What it does

- Takes a resume and job description as text input
- Calculates a similarity match score using TF-IDF and cosine similarity
- Extracts and compares technical skills using keyword-based NLP matching
- Shows matched skills vs missing skills side by side
- Runs through a simple web interface — no coding knowledge needed to use it

## Tech Stack

- **Python** — core language
- **scikit-learn** — TF-IDF vectorization and cosine similarity for match scoring
- **spaCy** — NLP setup for text processing
- **FastAPI** — REST API backend that exposes the matching logic
- **Streamlit** — frontend web interface for uploading and viewing results

## How it works

1. User pastes resume text and job description text into the Streamlit app
2. Streamlit sends this data to a FastAPI backend endpoint (`/analyze`)
3. The backend runs TF-IDF similarity scoring and skill-keyword extraction
4. Results (match score, matched skills, missing skills) are returned as JSON
5. Streamlit displays the results in a clean, readable format

## Project Structure

resume-matcher/
├── analyzer.py # Core ML logic: TF-IDF scoring + skill extraction
├── main.py # FastAPI backend with /analyze endpoint
├── app.py # Streamlit frontend
├── requirements.txt # Python dependencies

## How to run locally

1. Clone this repository
2. Create and activate a virtual environment
3. Install dependencies:
pip install -r requirements.txt
4. Start the backend:
uvicorn main:app --reload
5. In a second terminal, start the frontend:
streamlit run app.py


6. Open the Streamlit URL shown in the terminal (usually `http://localhost:8501`)

## Why this project

Built to demonstrate practical, full-stack data science skills — combining machine learning (scikit-learn), NLP (spaCy), API development (FastAPI), and frontend interfaces (Streamlit) in one working application, rather than an isolated notebook exercise.

## Future improvements

- Direct PDF upload instead of manual text pasting
- Semantic matching using sentence embeddings or LLM APIs for more accurate scoring
- Deployment to a live public URL

