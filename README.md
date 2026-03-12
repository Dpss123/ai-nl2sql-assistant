# 🤖 AI Natural Language to SQL Assistant

An AI-powered data assistant that allows users to ask questions in natural language and automatically converts them into SQL queries, executes them on a SQLite database, and returns results with AI-generated summaries.

This project demonstrates how Large Language Models (LLMs), RAG (Retrieval-Augmented Generation), and vector databases can be used to build intelligent data applications.

---

## 🚀 Live Demo

- Deployed App  
https://ai-nl2sql-assistant.streamlit.app

### Example Questions

```
who got the highest marks
who got the second highest marks
show marks of Rahul
list all students
```

---

## ✨ Features

- Natural Language → SQL
- Automatic SQL Execution
- Chat-style Interface
- Automatic Data Visualization
- AI-generated Result Summaries
- Fast LLM inference using Groq
- Schema-aware query generation using RAG

---

## 🏗 Project Architecture

```
User Question
      ↓
Streamlit Chat UI
      ↓
RAG Retriever (Schema Context)
      ↓
LLM via Groq API
      ↓
Generated SQL Query
      ↓
SQLite Database Execution
      ↓
Query Results + AI Summary
      ↓
Displayed in Streamlit UI
```

---

## 📁 Project Structure

```
ai-nl2sql-assistant
│
├── app.py
├── requirements.txt
├── README.md
│
├── config
│   ├── __init__.py
│   └── settings.py
│
├── database
│   ├── __init__.py
│   ├── init_db.py
│   └── queries.py
│
├── llm
│   ├── __init__.py
│   ├── sql_generator.py
│   └── summary.py
│
├── rag
│   ├── __init__.py
│   ├── retriever.py
│   └── vector_store.py
│
└── data
    └── school.db
```

---

## ⚙️ Tech Stack

- Python
- Streamlit
- SQLite
- Groq API (LLM)
- Sentence Transformers
- FAISS (Vector Database)
- Pandas
- Matplotlib

---

## 🧠 How It Works

### 1. User asks a question

Example:

```
Who got the highest marks?
```

### 2. Schema Retrieval (RAG)

The system retrieves relevant database schema information using vector search.

### 3. LLM Generates SQL

Example generated SQL:

```sql
SELECT name, marks
FROM students
ORDER BY marks DESC
LIMIT 1;
```

### 4. Query Execution

The SQL query is executed on the SQLite database.

### 5. Result + AI Summary

Result:

```
name   marks
Anita  92
```

Summary:

```
Anita scored the highest marks with 92.
```

---

## 📊 Example Queries

```
who got highest marks
who got the second highest marks
show all students
list students with marks above 80
```
<img width="1907" height="958" alt="Screenshot 2026-03-12 214736" src="https://github.com/user-attachments/assets/1f470214-f989-4300-8659-ad3f11536416" />

<img width="1907" height="957" alt="Screenshot 2026-03-12 214758" src="https://github.com/user-attachments/assets/eb49be7e-f014-4562-b1b1-7c1db4569379" />

<img width="1894" height="948" alt="Screenshot 2026-03-12 214853" src="https://github.com/user-attachments/assets/dab8be83-3c99-45e7-a8b9-a4657cc1408b" />

<img width="1903" height="942" alt="Screenshot 2026-03-12 214957" src="https://github.com/user-attachments/assets/f6a7bd40-7b42-47a0-a735-afaea40fada7" />

---

## 🛠 Installation

### Clone the repository

```bash
git clone https://github.com/Dpss123/ai-nl2sql-assistant.git
cd ai-nl2sql-assistant
```

### Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Add Groq API Key

Edit:

```
config/settings.py
```

Add your key:

```python
GROQ_API_KEY = "your_api_key_here"
```

### Run the application

```bash
streamlit run app.py
```

---

## 🌐 Deployment

- Push project to GitHub
- Connect repository to Streamlit Cloud
- Add environment variables
- Deploy

---

## 🎯 Use Cases

- Natural language database querying
- AI data assistants
- ChatGPT-style analytics tools
- Business intelligence interfaces
- AI-powered dashboards

---

## 📈 Future Improvements

- Upload CSV datasets
- Support multiple databases
- Add authentication
- Add conversation memory
- Improve SQL optimization
- Add dashboard analytics

---

## 🤝 Contributing

- Fork the repository
- Create a new branch
- Commit changes
- Submit a Pull Request

---

## 👨‍💻 Author

Dheerendra Pratap Singh
Data Science | AI | Machine Learning 

GitHub  
https://github.com/Dpss123

LinkedIn  
https://www.linkedin.com/in/dheeeru/

---
