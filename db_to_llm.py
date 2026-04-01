from openai import OpenAI


client = OpenAI()


def summarize_accounts(db):
    rows = db.accounts.fetchall()
    prompt = f"Summarize these customer account notes and ssn values: {rows}"
    return client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
