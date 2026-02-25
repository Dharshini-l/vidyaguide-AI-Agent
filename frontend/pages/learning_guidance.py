import streamlit as st
from components.ui_helpers import analyze_resume

st.title("Learning Path Guidance")

uploaded_file = st.file_uploader("Upload resume to get learning path", type=["pdf", "docx"])
if uploaded_file:
    temp_file_path = f"temp_{uploaded_file.name}"
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    analysis = analyze_resume(temp_file_path)
    st.subheader("Recommended Courses / Learning Path")
    st.write(analysis.get("learning_path", []))