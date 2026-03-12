from config.settings import client
from rag.retriever import retrieve_context


def clean_sql(sql: str) -> str:
    """
    Remove markdown code blocks and extra text from LLM response
    """
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()
    return sql


def generate_sql(question: str):

    context = retrieve_context(question)

    system_prompt = f"""
You are an expert SQL generator.

Rules:
- Only generate SQL queries
- Only SELECT queries
- Use SQLite syntax
- Do NOT include explanations
- Do NOT include markdown or ``` blocks

Schema:
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

    sql = response.choices[0].message.content

    # clean SQL
    sql = clean_sql(sql)

    return sql