import sqlite3
import pandas as pd
from config.settings import DB_PATH


def clean_sql(sql: str) -> str:
    """
    Remove markdown formatting from SQL
    """
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()
    return sql


def run_query(sql: str):

    sql = clean_sql(sql)

    conn = sqlite3.connect(DB_PATH)

    try:
        df = pd.read_sql_query(sql, conn)
    finally:
        conn.close()

    return df