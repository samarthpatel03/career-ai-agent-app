import streamlit as st
from app.agent.career_agent import run_career_agent
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
st.set_page_config(page_title="AI Career Agent", page_icon="🎯", layout="centered")

# --- Title and Description ---
st.markdown("""
<h1 style='text-align: center;'>🚀 AI Career Recommendation Agent</h1>
<p style='text-align: center; color: gray;'>Discover your ideal career path, must-have skills, and free resources using AI</p>
""", unsafe_allow_html=True)

# --- Input Box ---
with st.form("interest_form"):
    interests = st.text_input("🎓 What are your interests?", placeholder="e.g. robotics, finance, biology, gaming")
    submit = st.form_submit_button("Suggest Me a Career 🔍")

# --- Processing ---
if submit:
    if not interests.strip():
        st.warning("⚠️ Please enter at least one interest.")
    else:
        with st.spinner("Thinking like a career guru... 🤖"):
            try:
                result = run_career_agent(interests)
                st.success("Here's what I found! 🎯")

                with st.expander("🎯 Suggested Career Paths"):
                    st.markdown(f"<div style='padding:10px;'>{result['career']}</div>", unsafe_allow_html=True)

                with st.expander("🧠 Required Skills & Salary Insights"):
                    st.markdown(f"<div style='padding:10px;'>{result['skill_and_salary']}</div>", unsafe_allow_html=True)

                with st.expander("📚 Free Learning Resources"):
                    st.markdown(f"<div style='padding:10px;'>{result['resources']}</div>", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"❌ Something went wrong!\n\n{e}")
