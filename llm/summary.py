from config.settings import client

def generate_summary(question, df):

    if df.empty:
        return "No data found."

    prompt = f"""
Question: {question}

Data:
{df.to_string(index=False)}

Explain result in one short sentence.
"""

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {"role":"user","content":prompt}
        ],

        temperature=0.2
    )

    return response.choices[0].message.content.strip()