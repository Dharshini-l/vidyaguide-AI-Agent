from fastapi import APIRouter, UploadFile, File
from utils.ai_connector import extract_skills, recommend_career, learning_path
import os

router = APIRouter(prefix="/resume")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Upload endpoint
@router.post("/upload")
def upload_resume(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return {"message": f"{file.filename} uploaded successfully"}

# Analyze endpoint
@router.post("/analyze")
def analyze_resume(file: UploadFile = File(...)):
    content = file.file.read().decode("utf-8", errors="ignore")
    skills = extract_skills(content)
    careers = recommend_career(skills)
    path = learning_path(skills)
    return {
        "skills": skills,
        "career_suggestions": careers,
        "learning_path": path
    }