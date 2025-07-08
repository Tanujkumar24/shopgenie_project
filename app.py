from llm.groq_model import get_llm
from llm.prompts import comparison_prompt
from llm.parser_models import ProductComparison
from search.web_search import search_web
from data.youtube_client import search_youtube
from utils.email_service import send_email_report
from langchain_core.output_parsers import JsonOutputParser
import json

def main():
    query = input("Enter your product search query: ")
    email = input("Enter your email to receive results: ")

    print("\n🔍 Searching Web...")
    web_results = search_web(query)
    product_titles = [res["title"] for res in web_results]
    print(f"Found {len(product_titles)} products.")

    product_info = "\n\n".join([f"{i+1}. {title}" for i, title in enumerate(product_titles)])

    llm = get_llm()
    prompt = comparison_prompt.format(products_info=product_info)
    parser = JsonOutputParser(pydantic_object=ProductComparison)
    chain = prompt | llm | parser
    output = chain.invoke({"products_info": product_info})

    print("\n🧠 Product Comparison:")
    print(json.dumps(output, indent=2))

    print("\n📧 Sending email...")
    send_email_report(email, query, output)

    print("\n📺 YouTube Suggestions:")
    yt_results = search_youtube(query)
    for video in yt_results:
        print(f"- {video['title']}: {video['url']}")

if __name__ == "__main__":
    main()