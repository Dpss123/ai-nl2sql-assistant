from config.settings import client


def generate_summary(question, df):

    if df is None or df.empty:
        return "No data found for this question."

    question_lower = question.lower()

    # If result has only one row and one column
    if df.shape[0] == 1 and df.shape[1] == 1:
        value = df.iloc[0, 0]

        if "second" in question_lower or "2nd" in question_lower:
            return f"{value} has the second highest marks."

        if "highest" in question_lower or "top" in question_lower:
            return f"{value} has the highest marks."

        if "who" in question_lower:
            return f"The answer is {value}."

        return str(value)

    # If name and marks both present
    if "name" in df.columns and "marks" in df.columns:
        row = df.iloc[0]
        return f"{row['name']} scored {row['marks']} marks."

    # Limit rows sent to LLM
    preview_df = df.head(5)
    result_text = preview_df.to_string(index=False)

    prompt = f"""
You are a helpful data assistant.

User Question:
{question}

SQL Result:
{result_text}

Write ONE clear sentence summarizing the answer.
Use only the result data.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You summarize SQL results clearly."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()
