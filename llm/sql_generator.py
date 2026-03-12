from config.settings import client
from rag.retriever import retrieve_context


def clean_sql(sql_text):
    """
    Remove markdown formatting like ```sql ``` if the LLM returns it.
    """

    sql_text = sql_text.replace("```sql", "")
    sql_text = sql_text.replace("```", "")
    return sql_text.strip()


def generate_sql(question):

    context = retrieve_context(question)

    system_prompt = f"""
You are an expert SQLite SQL generator.

Your job is to convert a user question into a correct SQL query.

Rules:
- Only generate SELECT queries
- Use SQLite syntax only
- Do NOT include explanations
- Do NOT include markdown like ```sql
- Return ONLY the SQL query
- Use the provided database schema
- When questions ask about highest, maximum, lowest, or rankings,
  return both the name AND the value column (example: name, marks)

Database Schema:
{context}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        temperature=0
    )

    sql = response.choices[0].message.content.strip()

    return clean_sql(sql)
