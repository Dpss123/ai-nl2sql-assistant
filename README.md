# 🤖 AI NL2SQL Data Assistant

An AI-powered Natural Language to SQL assistant that allows users to query databases using simple English questions.  
The system converts natural language into SQL queries using an LLM and retrieves results from a database in real time.

---

## 🌐 Live Demo

🔗 **App URL:**  
https://yourusername-ai-nl2sql-assistant.streamlit.app

---

## 🚀 Features

- Natural Language → SQL query generation
- LLM-powered query generation using Groq API
- Retrieval-Augmented Generation (RAG) for schema understanding
- SQLite database integration
- Interactive web interface using Streamlit
- Automatic SQL result visualization
- Safe SQL execution (SELECT-only queries)

---

## 🧠 How It Works

1. User enters a question in natural language  
2. RAG retrieves relevant database schema context  
3. LLM generates a valid SQL query  
4. Query runs on the SQLite database  
5. Results are displayed in an interactive table

---

## 🏗️ Project Architecture


User Question
↓
Streamlit UI
↓
RAG Retriever (Schema Context)
↓
LLM (Groq API)
↓
Generated SQL
↓
SQLite Database
↓
Query Results
↓
Streamlit UI


---

## 📂 Project Structure


ai-nl2sql-assistant
│
├── app.py
│
├── config
│ ├── init.py
│ └── settings.py
│
├── database
│ ├── init.py
│ ├── init_db.py
│ └── queries.py
│
├── llm
│ ├── init.py
│ ├── sql_generator.py
│ └── summary.py
│
├── rag
│ ├── init.py
│ ├── retriever.py
│ └── vector_store.py
│
├── data
│ └── school.db
│
├── requirements.txt
└── README.md


---

## ⚙️ Tech Stack

- **Python**
- **Streamlit**
- **Groq LLM API**
- **SQLite**
- **Sentence Transformers**
- **FAISS Vector Database**
- **Pandas**

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ai-nl2sql-assistant.git
cd ai-nl2sql-assistant

Create a virtual environment:

python -m venv venv

Activate environment:

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
🔑 Add API Key

Create a Streamlit secrets file:


.streamlit/secrets.toml


Add your Groq API key:

GROQ_API_KEY = "your_api_key_here"
▶️ Run the Application
streamlit run app.py

Then open:


http://localhost:8501

💬 Example Questions

Try asking:


highest marks
average marks
students in CSE
list all departments
students older than 20

📸 Screenshots

Example interface:


User Question → "highest marks"

Generated SQL:

SELECT MAX(marks) FROM students;

Result:

92

🎯 Use Cases

Data analysis without SQL knowledge

Natural language database querying

AI-powered analytics dashboards

Educational SQL learning tools

🔒 Security

The system only allows SELECT queries to prevent database modification.

📈 Future Improvements

Multi-database support (PostgreSQL, MySQL)

Advanced RAG with larger schema context

Query explanation for learning SQL

Role-based query permissions

Support for large enterprise databases

👨‍💻 Author

Dheerendra Pratap Singh

B.Tech Computer Science Engineering
AI / ML / LLM Enthusiast

GitHub:
https://github.com/Dpss123

LinkedIn:
https://www.linkedin.com/in/dheeeru/
