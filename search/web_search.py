from langchain_community.tools.tavily_search import TavilySearchResults

def search_web(query: str):
    search_tool = TavilySearchResults(k=6)
    results = search_tool.run(query)
    return results