from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.agent.career_agent import run_career_agent
from app.schemas.request import CareerQuery

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {"message": "Agent is running"}

@app.post("/suggest")  # ✅ POST instead of GET
def suggest_career(query: CareerQuery):
    result = run_career_agent(query.interests)
    return result



# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.agent.career_agent import run_career_agent
# from app.schemas.request import CareerQuery

# app=FastAPI()

# # app.add_middleware.allow_origins=["*"],
# # allow_credentials=True,
# # allow_methods=["*"],
# # allow_headers=["*"]


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )


# @app.get("/")
# def root():
#     return {"message": "Agent is running"}


# @app.get("/suggest")
# def suggest_career(query: CareerQuery):
#     result=run_career_agent(query.interests)
#     return result


