import streamlit as st
from components.ui_helpers import get_career_suggestions

st.title("Career Dashboard")

career_data = get_career_suggestions()
st.subheader("Recommended Careers")
st.write(career_data.get("career_suggestions", []))