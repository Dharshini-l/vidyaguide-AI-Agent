from fastapi import FastAPI
from routes import resume, career

app = FastAPI()

# Include API routers
app.include_router(resume.router)
app.include_router(career.router)

@app.get("/")
def home():
    return {"message": "Backend is running!"}