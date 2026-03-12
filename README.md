🤖 AI Natural Language to SQL Assistant

An AI-powered data assistant that allows users to ask questions in natural language and automatically converts them into SQL queries, executes them on a SQLite database, and returns results with AI-generated summaries.

This project demonstrates how Large Language Models (LLMs), RAG (Retrieval-Augmented Generation), and vector databases can be used to build intelligent data applications.

🚀 Live Demo

🔗 Deployed App:
https://ai-nl2sql-assistant.streamlit.app

Example questions you can ask:

who got the highest marks
who got the second highest marks
show marks of Rahul
list all students
✨ Features

🧠 Natural Language → SQL

📊 Automatic SQL Execution

💬 Chat-style Interface

📈 Automatic Data Visualization

🧾 AI-generated Result Summaries

⚡ Fast LLM inference using Groq

🗂 Schema-aware query generation using RAG

🏗 Project Architecture

User Question
⬇
Streamlit Chat UI
⬇
RAG Retriever (Schema Context)
⬇
LLM via Groq API
⬇
Generated SQL Query
⬇
SQLite Database Execution
⬇
Query Results + AI Summary
⬇
Displayed in Streamlit UI

📁 Project Structure
ai-nl2sql-assistant
│
├── app.py                     # Main Streamlit application
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
├── config
│   ├── __init__.py
│   └── settings.py            # API keys and configuration
│
├── database
│   ├── __init__.py
│   ├── init_db.py             # Creates SQLite database
│   └── queries.py             # Executes SQL queries
│
├── llm
│   ├── __init__.py
│   ├── sql_generator.py       # Converts natural language → SQL
│   └── summary.py             # Generates AI summaries
│
├── rag
│   ├── __init__.py
│   ├── retriever.py           # Retrieves schema context
│   └── vector_store.py        # FAISS vector database
│
└── data
    └── school.db              # SQLite database
⚙️ Tech Stack

Python

Streamlit

SQLite

Groq API (LLM)

Sentence Transformers

FAISS (Vector Database)

Pandas

Matplotlib

🧠 How It Works
1️⃣ User asks a question

Example:

Who got the highest marks?
2️⃣ Schema Retrieval (RAG)

The system retrieves relevant database schema information using vector search.

3️⃣ LLM Generates SQL

Example generated SQL:

SELECT name, marks 
FROM students 
ORDER BY marks DESC 
LIMIT 1;
4️⃣ Query Execution

The SQL query is executed on the SQLite database.

5️⃣ Result + AI Summary

Result:

name	marks
Anita	92

Summary:

Anita scored the highest marks with 92.

📊 Example Queries

Try asking:

who got highest marks
who got the second highest marks
show all students
list students with marks above 80
🛠 Installation
1️⃣ Clone the repository
git clone https://github.com/Dpss123/ai-nl2sql-assistant.git
cd ai-nl2sql-assistant
2️⃣ Create virtual environment
python -m venv venv

Activate it:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Add your Groq API Key

Edit:

config/settings.py

Add your key:

GROQ_API_KEY = "your_api_key_here"
5️⃣ Run the application
streamlit run app.py
🌐 Deployment

The app is deployed using Streamlit Cloud.

Steps:

Push project to GitHub

Connect repository to Streamlit Cloud

Add environment variables

Deploy

🎯 Use Cases

Natural language database querying

AI data analysis assistants

ChatGPT-style analytics tools

Business intelligence interfaces

AI-powered dashboards

📈 Future Improvements

Upload CSV datasets

Support multiple databases

Add authentication

Add conversation memory

Improve SQL optimization

Add dashboard analytics

🤝 Contributing

Contributions are welcome!

Steps:

Fork the repository

Create a new branch

Commit changes

Submit a Pull Request
