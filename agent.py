from langchain.agents import initialize_agent, AgentType
from langchain_openai import OpenAI
from tools import tools
import os
from dotenv import load_dotenv

# For environmental variable
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

# Define the LLM
llm = OpenAI(temperature=0.6, openai_api_key=openai_api_key)

# Define the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=True
)