from langchain_core.output_parsers import JsonOutputParser, StrOutputParser, XMLOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")    

llm = ChatOpenAI(model="gpt-5-nano")

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert resume writer for GenAI and Data Engineering roles."
    ),
    (
        "human",
        """
        Convert this project into 3 strong resume bullet points.
        Project: {project_description}
        Target Role: {target_role}
        """
    )
])
chain = prompt | llm | StrOutputParser()
result = chain.invoke({
    "project_description": """
    Built a Text-to-SQL chatbot using OpenAI, LangChain, AWS Lambda,
    ECS Fargate, RDS PostgreSQL, and Secrets Manager.
    """,
    "target_role": "GenAI Data Engineer"
})

print(result)
