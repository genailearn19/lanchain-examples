from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import create_agent
from langchain.tools import tool


# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-5-nano"
)

@tool
def get_weather(location: str) -> str:
    """
     Get current weather for a given city or location.
    Use this when the user asks about weather.
    """
    # Placeholder function to simulate fetching weather data
    return f"The current weather in {location} is sunny with a temperature of 25°C."

def search_company_knowledge_base(query: str) -> str:
    """
    Search the company's knowledge base for relevant information.
    Use this when the user asks about company policies, procedures, or other internal information.
    """
    # Placeholder function to simulate searching a knowledge base
    return f"Search results for '{query}': [Company Policy Document], [Internal Wiki Page], [FAQ Section]."

tools = [get_weather, search_company_knowledge_base]

agent =create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
    You are a helpful assistant.
    Use tools whenever the user's question requires external or company-specific information.
    If no tool is needed, answer directly.""",
    debug=True)

response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "can you provide company leave policy?"
        }
    ]
})
print(response["messages"][-1].content)