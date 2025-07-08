import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    return ChatGroq(
        model="mixtral-8x7b-32768",
        api_key=os.getenv("GROQ_API_KEY")
    )