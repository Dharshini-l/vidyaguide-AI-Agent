import requests
import streamlit as st

BACKEND_URL = "http://127.0.0.1:8001"

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if uploaded_file is not None:
    st.success("✅ File uploaded successfully")

    if st.button("🔍 Analyze Resume"):
        with st.spinner("Analyzing your resume... Please wait ⏳"):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/resume/analyze",
                    files={"file": uploaded_file}
                )

                if response.status_code == 200:
                    result = response.json()

                    st.success("✅ Analysis Completed")

                    st.subheader("📊 Result:")
                    st.json(result)

                else:
                    st.error(f"❌ Backend Error: {response.status_code}")
                    st.write(response.text)

            except Exception as e:
                st.error("🚨 Cannot connect to backend")
                st.write(str(e))