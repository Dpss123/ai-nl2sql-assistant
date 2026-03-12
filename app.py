import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

from database.init_db import init_db
from database.queries import run_query
from llm.sql_generator import generate_sql
from llm.summary import generate_summary


#  PAGE CONFIG 
st.set_page_config(
    page_title="AI Data Assistant",
    page_icon="🤖",
    layout="wide"
)

init_db()

#  CUSTOM CSS 
st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

.gradient-title {
    font-size:42px;
    font-weight:800;
    text-align:center;
    background: linear-gradient(90deg,#4A90E2,#8E44AD,#E84393);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.subtitle {
    text-align:center;
    color:gray;
    margin-bottom:25px;
}

.card {
    background:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}

.stChatMessage {
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)


#  HEADER 
st.markdown("<div class='gradient-title'>🤖 AI Natural Language Data Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Ask questions about your database using natural language</div>", unsafe_allow_html=True)

st.divider()


#  SIDEBAR 
with st.sidebar:

    st.title("🧠 AI Tools")

    st.markdown("### Example Questions")

    st.markdown("""
    - who got the highest marks  
    - who got second highest marks  
    - show marks of Rahul  
    - list all students  
    """)

    st.divider()

    st.markdown("### Database Info")

    st.write("Tables Available:")
    st.write("- students")
    st.write("- departments")

    st.divider()

    st.info("This AI assistant converts natural language into SQL queries.")


#  DATABASE PREVIEW 
col1, col2 = st.columns(2)

with col1:

    st.markdown("### 🎓 Students")

    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.dataframe(run_query("SELECT * FROM students"), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)


with col2:

    st.markdown("### 🏫 Departments")

    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.dataframe(run_query("SELECT * FROM departments"), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

st.divider()


#  CHAT HISTORY 
if "chat" not in st.session_state:
    st.session_state.chat = []


# typing animation
def typewriter(text):

    container = st.empty()

    displayed = ""

    for char in text:
        displayed += char
        container.markdown(displayed)
        time.sleep(0.01)


for msg in st.session_state.chat:

    if msg["role"] == "user":

        st.chat_message("user").markdown(msg["content"])

    else:

        with st.chat_message("assistant"):

            # animated summary
            typewriter(msg["summary"])

            # SQL expander
            with st.expander("🧠 Generated SQL"):
                st.code(msg["sql"], language="sql")

            # result table
            st.subheader("📊 Result")
            st.dataframe(msg["df"], use_container_width=True)

            df = msg["df"]

            # visualization
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


#  USER INPUT 
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
