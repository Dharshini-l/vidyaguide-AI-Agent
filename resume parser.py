import streamlit as st
import pandas as pd
import nltk
import spacy
from PyPDF2 import PdfReader
from docx import Document
import openai

nltk.download('punkt')
nlp = spacy.load("en_core_web_sm")

openai.api_key = "agentic @i"

skills_db = [
    "python", "java", "c++", "machine learning", "deep learning",
    "data analysis", "sql", "html", "css", "javascript", "communication", "teamwork"
]

def parse_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

def parse_docx(file):
    doc = Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def extract_skills(text):
    text_lower = text.lower()
    extracted = [skill for skill in skills_db if skill in text_lower]
    return extracted

def recommend_career(skills):
    prompt = f"Given these skills: {skills}, recommend top career paths"
    missing = list(set(target)-set(extracted))
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def skill_gap(extracted, target):
    missing = list(set(target) - set(extracted))
    return missing

def learning_recommendations(gaps):
    prompt = f"Suggest online courses or resources to learn these skills: {gaps}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

st.title("💼 AI Resume Analysis & Career Recommendations")

uploaded_file = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        resume_text = parse_pdf(uploaded_file)
    else:
        resume_text = parse_docx(uploaded_file)

    st.subheader("Parsed Resume Text")
    st.text_area("Resume Text", resume_text, height=300)

    skills = extract_skills(resume_text)
    st.subheader(" Extracted Skills")
    st.write(skills if skills else "No skills found from the database.")

    if skills:
        career_suggestions = recommend_career(skills)
        st.subheader("Career Recommendations")
        st.write(career_suggestions)

    target_skills = ["python", "machine learning", "deep learning", "sql"]
    gaps = skill_gap(skills, target_skills)
    st.subheader(" Skill Gap Analysis")
    st.write("Skills to learn:", gaps if gaps else "No gaps. You are ready for target roles!")

    if gaps:
        recommendations = learning_recommendations(gaps)
        st.subheader(" Learning Recommendations")
        st.write(recommendations)

    st.subheader("Customize AI Suggestions")
    user_prompt = st.text_area("Add your custom instructions for AI", "")
    if user_prompt and skills:
        custom_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"{user_prompt} based on these skills {skills}"}]
        )
        st.subheader("AI Response for Custom Prompt")
        st.write(custom_response['choices'][0]['message']['content'])
