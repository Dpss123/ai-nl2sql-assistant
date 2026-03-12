from config.settings import client


def generate_summary(question, df):

    if df.empty:
        return "No data found for this question."

    result_text = df.to_string(index=False)

    prompt = f"""
You are a data assistant.

Based ONLY on the SQL result below, answer the user's question in ONE short sentence.

User Question:
{question}

SQL Result:
{result_text}

Rules:
- Use only the result data
- Do not guess or add information
- Give a clear answer
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You summarize database query results."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()
        ],

        temperature=0.2
    )

    return response.choices[0].message.content.strip()
