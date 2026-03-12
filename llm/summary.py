from config.settings import client


def generate_summary(question, df):

    # If no data
    if df is None or df.empty:
        return "No data found for this question."

    # If only one value result
    if df.shape[0] == 1 and df.shape[1] == 1:
        value = df.iloc[0, 0]
        column = df.columns[0]
        return f"The {column} is {value}."

    # Limit rows sent to LLM (avoid token overflow)
    preview_df = df.head(5)

    result_text = preview_df.to_string(index=False)

    prompt = f"""
You are an AI data analyst.

Your job is to summarize a SQL query result.

User Question:
{question}

SQL Result:
{result_text}

Instructions:
- Answer in ONE short sentence
- Use ONLY the SQL result
- Do NOT guess information
- If multiple rows exist, summarize the key insight
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You summarize SQL query results clearly and accurately."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()