from langchain_core.runnables import RunnableSequence
from app.chains.interest_chain import get_interest_chain
from app.chains.skill_chain import get_skill_chain
from app.chains.resource_chain import get_resource_chain

interest_chain=get_interest_chain()
resource_chain=get_resource_chain()
skill_chain=get_skill_chain()

def run_career_agent(interests: str) -> dict:
    careers_text = interest_chain.invoke({"interest": interests}).content.strip()
    skills_text = skill_chain.invoke({"careers": careers_text}).content.strip()
    resources_text = resource_chain.invoke({"careers": careers_text}).content.strip()


    return{
        "career": careers_text,
        "skill_and_salary": skills_text,
        "resources": resources_text
    }