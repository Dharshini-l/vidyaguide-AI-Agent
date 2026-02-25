import requests

BACKEND_URL = "http://127.0.0.1:8000"

def upload_resume(file_path):
    """Uploads resume to backend"""
    with open(file_path, "rb") as f:
        files = {"file": f}   # Must match FastAPI parameter
        response = requests.post(f"{BACKEND_URL}/resume/upload", files=files)
    return response.json()

def analyze_resume(file_path):
    """Analyze resume via backend API"""
    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(f"{BACKEND_URL}/resume/analyze", files=files)
    return response.json()

def get_career_suggestions():
    """Get career suggestions from backend"""
    response = requests.get(f"{BACKEND_URL}/career/suggestions")
    return response.json()