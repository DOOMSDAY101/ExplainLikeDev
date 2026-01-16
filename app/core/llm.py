from dotenv import load_dotenv
import os

load_dotenv()

from langchain_ollama import ChatOllama

def get_llm():
    """
    Returns an LLM instance based on environment configuration.
    """

    provider = os.getenv("LLM_PROVIDER", "ollama")

    if provider == "ollama":
        return ChatOllama(
            model=os.getenv("OLLAMA_MODEL", "llama3.2:3b"),
            temperature=0.3
        )
    

    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
