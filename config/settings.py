from groq import Groq
import streamlit as st

DB_PATH = "data/school.db"

client = Groq(api_key=st.secrets["GROQ_API_KEY"])