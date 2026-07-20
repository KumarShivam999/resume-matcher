from fastapi import FastAPI
from pydantic import BaseModel
from analyzer import analyze

app = FastAPI()

class MatchRequest(BaseModel):
    resume_text: str
    jd_text: str

@app.get("/")
def home():
    return {"message": "Resume Matcher API is running"}

@app.post("/analyze")
def analyze_resume(request: MatchRequest):
    result = analyze(request.resume_text, request.jd_text)
    return result