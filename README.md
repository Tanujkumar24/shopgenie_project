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

> 📌 Replace these image paths with your own screenshots (put images in an `images/` folder in your repo).

### 1️⃣ Streamlit - Product Query
![Search Query](https://github.com/Tanujkumar24/shopgenie_project/blob/main/shop_result1.png)

### 2️⃣ Product Comparison Results
![Comparison Output](https://github.com/Tanujkumar24/shopgenie_project/blob/main/shop_result2.png)

### 3️⃣ Email Sent Confirmation
![Email Sent](https://github.com/Tanujkumar24/shopgenie_project/blob/main/shop_result4.png
)
![Email Sent](https://github.com/Tanujkumar24/shopgenie_project/blob/main/shop_result5.png)

### 4️⃣ YouTube Suggestions
![YouTube](https://github.com/Tanujkumar24/shopgenie_project/blob/main/shop_result3.png)

---

## 📁 Project Structure

```
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
```

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/shopgenie.git
cd shopgenie
```

### 2. Create a virtual environment

```bash
python -m venv tenv
# On Windows
tenv\Scripts\activate
# On Mac/Linux
source tenv/bin/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your `.env` file

Create a `.env` file in the root directory and add the following:

```
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
YOUTUBE_API_KEY=your_youtube_api_key
SMTP_USER=your_email@gmail.com
SMTP_PASS=your_app_password
```

> ⚠️ Use an app password if you're using Gmail (required for SMTP login).

### 5. Run the CLI version

```bash
python app.py
```

### 6. Run the Streamlit frontend

```bash
streamlit run frontend/streamlit_app.py
```

---

## ⚙️ Tech Stack

- **Python 3.10+**
- [LangChain](https://www.langchain.com/)
- [Groq](https://groq.com/)
- [Tavily](https://www.tavily.com/)
- [YouTube Data API](https://developers.google.com/youtube/v3)
- [Streamlit](https://streamlit.io/)
- [Pydantic](https://docs.pydantic.dev/)

---

## 💡 Future Enhancements

- Integration with Amazon/Flipkart APIs  
- Voice assistant for product query input  
- User authentication and history tracking  
- PDF export for product reports  

---

## 👨‍💻 Author

**Tanujkumar Mangalapally**  
📧 tanuj.mangalapally@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/tanujkumar24)

---

## ⭐ If you like it, give it a star and share!
