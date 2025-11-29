import os
from tavily import TavilyClient

def get_search_tool():
    tavily_key = os.getenv("TAVILY_API_KEY")

    if not tavily_key:
        raise ValueError("Erro: TAVILY_API_KEY não foi encontrada. Use .env ou export.")

    return TavilyClient(api_key=tavily_key)
