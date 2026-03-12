from config.settings import client


def generate_summary(question, df):

    # If dataframe empty
    if df is None or df.empty:
        return "No data found for this question."

    # If single value
    if df.shape[0] == 1 and df.shape[1] == 1:
        column = df.columns[0]
        value = df.iloc[0, 0]

        # if column is name → answer directly
        if column.lower() == "name":
            return f"The answer is {value}."

        return f"The {column} is {value}."

    # Limit rows sent to LLM
    preview_df = df.head(5)

    result_text = preview_df.to_string(index=False)

    prompt = f"""
You are a data assistant.

A SQL query was executed and produced the result below.

User Question:
{question}

SQL Result:
{result_text}

Rules:
- Answer using ONLY the SQL result
- If the result shows a name, respond with that name as the answer
- Do NOT say information is missing if the answer is visible
- Respond in ONE clear sentence
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You summarize SQL results for users."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()
