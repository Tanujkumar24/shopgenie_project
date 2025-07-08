import streamlit as st
from llm.groq_model import get_llm
from llm.prompts import comparison_prompt
from llm.parser_models import ProductComparison
from search.web_search import search_web
from data.youtube_client import search_youtube
from utils.email_service import send_email_report
from langchain_core.output_parsers import JsonOutputParser
import json

st.set_page_config(page_title="ShopGenie", layout="wide")
st.title("🛍️ ShopGenie - Mobile Product Comparison Assistant")

query = st.text_input("🔎 Enter product search query", "Best phones under 30000 INR")
email = st.text_input("📧 Enter your email to receive results")

if st.button("Compare Products"):
    with st.spinner("Searching web and analyzing..."):
        try:
            web_results = search_web(query)
            product_titles = [res["title"] for res in web_results]
            product_info = "\n\n".join([f"{i+1}. {title}" for i, title in enumerate(product_titles)])

            llm = get_llm()
            prompt = comparison_prompt.format(products_info=product_info)
            parser = JsonOutputParser(pydantic_object=ProductComparison)
            chain = prompt | llm | parser
            output = chain.invoke({"products_info": product_info})

            st.subheader("📊 Product Comparison")
            st.json(output)

            if email:
                send_email_report(email, query, output)
                st.success("📧 Email sent!")

            st.subheader("📺 YouTube Suggestions")
            yt_results = search_youtube(query)
            for video in yt_results:
                st.markdown(f"- [{video['title']}]({video['url']})")
        except Exception as e:
            st.error(f"Something went wrong: {e}")