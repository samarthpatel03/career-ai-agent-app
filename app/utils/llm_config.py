# from langchain_openai import ChatOpenAI
# from app.config import OPENAI_API_KEY

# def get_openai_llm(model='gpt-3.5-turbo'):
#     return ChatOpenAI(
#         model=model,
#         temperature=0.3,
#         openai_api_key=OPENAI_API_KEY
#     )


# from langchain_google_genai import ChatGoogleGenerativeAI
# import os
# from dotenv import load_dotenv

# load_dotenv()

# def get_openai_llm():
#     return ChatGoogleGenerativeAI(
#         model="gemini-pro",
#         google_api_key=os.getenv("GEMINI_API_KEY"),
#         temperature=0.3
#     )



from langchain_groq import ChatGroq
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def get_openai_llm(model="llama-3.1-8b-instant"):  # you can also use llama3-8b-8192 or gemma-7b-it
    return ChatGroq(
        api_key=st.secrets["GROQ_API_KEY"],
        model_name=model,
        temperature=0.3
    )
