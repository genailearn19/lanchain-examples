from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model="gpt-5-nano")
@tool
def get_current_weather(location: str) -> str:
    """
    Get the current weather in a given location.
    """
    # For demonstration purposes, we'll return a hardcoded response.
    # In a real implementation, you would call a weather API here.
    return f"The current weather in {location} is sunny with a temperature of 25°C."

@tool
def get_company_info(company_name: str) -> str:
    """
    Get information about a company.
    """
    # For demonstration purposes, we'll return a hardcoded response.
    # In a real implementation, you would call a company info API here.
    return f"{company_name} is a leading company in the tech industry, known for its innovative products and services."

agent = create_agent(model=model, 
                     tools=[get_current_weather, get_company_info],
                     system_prompt=
                     """ \
                     You are a helpful assistant that can provide weather
                       information and company details.
                       """)


response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "What is the weather in Hyderabad?"
        }
    ]
})

print(response["messages"][-1].content)