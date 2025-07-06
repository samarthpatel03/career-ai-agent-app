# 🧠 AI Career Advisor Agent

This is an AI-powered Career Advisor built using **LangChain**, **FastAPI**, and **GROQ LLMs**. It takes your interests and suggests suitable career paths, required skills, salary estimates, and top learning resources — all in seconds.

You can also run this project with a **Streamlit UI** for a beautiful and interactive web experience.

---

## 🚀 Features

- 🔍 Input user interests to get personalized career suggestions
- 🧠 Uses LangChain + Groq (Mixtral 8x7B or other supported models)
- 💼 Shows:
  - Career Options
  - Required Skills + Salary (INR)
  - Free Learning Resources (Courses & Platforms)
- 🌐 REST API with FastAPI
- 🎨 Frontend via Streamlit (optional)
- 📦 Modular and clean codebase
- 🛡️ API key protection via `.env`

---

## 📁 Project Structure

AiAgents/
├── app/
│ ├── agent/
│ │ └── career_agent.py
│ ├── chains/
│ │ ├── interest_chain.py
│ │ ├── resource_chain.py
│ │ └── skill_chain.py
│ ├── schemas/
│ │ └── request.py
│ └── utils/
│ └── llm_config.py
├── main.py # FastAPI app
├── streamlit_app.py # Streamlit frontend (optional)
├── .env.example # Sample API keys file
├── .gitignore
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-career-agent.git
cd ai-career-agent
2. Create Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate  # for Linux/macOS
venv\Scripts\activate     # for Windows

pip install -r requirements.txt
3. Add Your API Keys
Create a .env file using the provided example:

cp .env.example .env
Open .env and add your API keys:

GROQ_API_KEY=your-groq-api-key-here
# Or any other LLM you use, like:
# OPENAI_API_KEY=your-openai-api-key-here
4. Run the FastAPI Backend
uvicorn main:app --reload
Visit: http://127.0.0.1:8000

Root endpoint shows: {"message": "Agent is running"}

API endpoint for suggestions: POST /suggest

5. Run the Streamlit Frontend (Optional)
streamlit run streamlit_app.py