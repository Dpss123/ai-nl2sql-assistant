import streamlit as st
from database.init_db import init_db
from database.queries import run_query
from llm.sql_generator import generate_sql
from llm.summary import generate_summary

st.set_page_config(page_title="AI Data Assistant", layout="wide")

init_db()

st.title("🤖 AI Data Assistant")

col1,col2 = st.columns(2)

with col1:
    st.subheader("Students")
    st.dataframe(run_query("SELECT * FROM students"))

with col2:
    st.subheader("Departments")
    st.dataframe(run_query("SELECT * FROM departments"))

if "chat" not in st.session_state:
    st.session_state.chat = []

for msg in st.session_state.chat:

    if msg["role"]=="user":
        st.chat_message("user").markdown(msg["content"])

    else:
        with st.chat_message("assistant"):

            st.success(msg["summary"])
            st.code(msg["sql"],language="sql")
            st.dataframe(msg["df"])

question = st.chat_input("Ask about the database")

if question:

    st.session_state.chat.append({"role":"user","content":question})

    sql = generate_sql(question)

    df = run_query(sql)

    summary = generate_summary(question, df)

    st.session_state.chat.append({
        "role":"assistant",
        "sql":sql,
        "df":df,
        "summary":summary
    })

    st.rerun()