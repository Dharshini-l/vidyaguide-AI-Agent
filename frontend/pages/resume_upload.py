import streamlit as st
from components.ui_helpers import upload_resume, analyze_resume

st.title("Upload Your Resume")

uploaded_file = st.file_uploader("Choose your resume (PDF/DOCX)", type=["pdf", "docx"])
if uploaded_file:
    # Save temporarily
    temp_file_path = f"temp_{uploaded_file.name}"
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Call backend upload API
    result = upload_resume(temp_file_path)
    st.success(result.get("message", "File uploaded"))

    # Call backend analyze API
    analysis = analyze_resume(temp_file_path)
    st.subheader("Skills")
    st.write(analysis.get("skills", []))
    st.subheader("Career Suggestions")
    st.write(analysis.get("career_suggestions", []))
    st.subheader("Learning Path")
    st.write(analysis.get("learning_path", []))