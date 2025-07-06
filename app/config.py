from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]