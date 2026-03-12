import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from database.init_db import init_db
from database.queries import run_query
from llm.sql_generator import generate_sql
from llm.summary import generate_summary


st.set_page_config(
    page_title="AI Data Assistant",
    page_icon="🤖",
    layout="wide"
)

init_db()

st.title("🤖 AI Data Assistant")
st.markdown("Ask questions about the database using **natural language**.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎓 Students")
    st.dataframe(run_query("SELECT * FROM students"), use_container_width=True)

with col2:
    st.subheader("🏫 Departments")
    st.dataframe(run_query("SELECT * FROM departments"), use_container_width=True)

st.divider()

if "chat" not in st.session_state:
    st.session_state.chat = []

for msg in st.session_state.chat:

    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])

    else:
        with st.chat_message("assistant"):

            # summary
            st.success(msg["summary"])

            # SQL
            with st.expander("🧠 Generated SQL"):
                st.code(msg["sql"], language="sql")

            # result table
            st.subheader("📊 Result")
            st.dataframe(msg["df"], use_container_width=True)

            # auto visualization
            df = msg["df"]

            if not df.empty and df.shape[1] >= 2:

                numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

                if len(numeric_cols) > 0:

                    st.subheader("📈 Visualization")

                    label_col = df.columns[0]
                    value_col = numeric_cols[0]

                    fig, ax = plt.subplots()

                    ax.bar(df[label_col], df[value_col])

                    ax.set_xlabel(label_col)
                    ax.set_ylabel(value_col)

                    st.pyplot(fig)

# USER INPUT 
question = st.chat_input("Ask a question about the database...")

if question:

    st.session_state.chat.append({
        "role": "user",
        "content": question
    })

    try:

        sql = generate_sql(question)

        df = run_query(sql)

        summary = generate_summary(question, df)

        st.session_state.chat.append({
            "role": "assistant",
            "sql": sql,
            "df": df,
            "summary": summary
        })

        st.rerun()

    except Exception as e:

        st.error("❌ Error processing your query.")