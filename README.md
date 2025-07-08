# 🛍️ ShopGenie - Smart Product Comparison Assistant

**ShopGenie** is an AI-powered assistant that helps users compare mobile products based on specs, reviews, ratings, and YouTube videos. Built with **LangChain**, **Groq**, and **Streamlit**, this assistant performs intelligent analysis of product listings and delivers comparison reports to your inbox.

---

## 🚀 Features

- 🔍 Real-time web product search
- 🧠 AI-based product comparison using LangChain + Groq
- 📧 Auto-email report delivery with specs, ratings & reviews
- 📺 YouTube video suggestions using YouTube Data API
- 🖥️ Interactive Streamlit frontend
- ⚙️ Clean, modular Python code ready for production

---

## 🖼️ Screenshots

> 📌 Replace these image paths with your own screenshots (in an `images/` folder).

### 1️⃣ Streamlit - Product Query
![Search Query](images/streamlit_query.png)

### 2️⃣ Product Comparison Results
![Comparison Output](images/comparison_output.png)

### 3️⃣ Email Sent Confirmation
![Email Sent](images/email_sent.png)

### 4️⃣ YouTube Suggestions
![YouTube](images/youtube_suggestions.png)

---

## 📁 Project Structure

```text
shopgenie/
│
├── app.py                      # CLI interface
├── frontend/
│   └── streamlit_app.py        # Streamlit frontend
├── llm/
│   ├── groq_model.py           # LLM integration using Groq API
│   ├── prompts.py              # Prompt template for comparison
│   └── parser_models.py        # Output model using Pydantic
├── search/
│   └── web_search.py           # Tavily-powered web search
├── data/
│   └── youtube_client.py       # YouTube Data API integration
├── utils/
│   └── email_service.py        # Email reporting service
├── .env                        # Environment variables (not tracked)
├── .gitignore                  # Ignore compiled & env files
├── requirements.txt            # Project dependencies
└── README.md
## 🛠️ Setup Instructions
###1. Clone the repository
git clone https://github.com/yourusername/shopgenie.git
cd shopgenie

