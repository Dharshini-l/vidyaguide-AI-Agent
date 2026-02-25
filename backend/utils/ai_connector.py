# utils/ai_connector.py

# 🚀 spaCy remove pannirukom for fast loading

SKILL_SET = ["Python", "SQL", "Excel", "Power BI", "Pandas", "Data Analysis"]

def extract_skills(text):
    if not text:
        return []
    skills = [skill for skill in SKILL_SET if skill.lower() in text.lower()]
    return skills

def recommend_career(skills):
    if "Python" in skills and "SQL" in skills:
        return ["Data Analyst", "Data Scientist"]
    elif "Excel" in skills:
        return ["Business Analyst"]
    else:
        return ["Software Engineer"]

def learning_path(skills):
    path = []
    if "Python" not in skills:
        path.append("Learn Python Basics")
    if "SQL" not in skills:
        path.append("Learn SQL Basics")
    if "Pandas" not in skills:
        path.append("Pandas Course")
    return path