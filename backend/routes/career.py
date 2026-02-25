from fastapi import APIRouter

router = APIRouter(prefix="/career")

@router.get("/suggestions")
def career_suggestions():
    return {"career_suggestions": ["Data Analyst", "Software Engineer"]}