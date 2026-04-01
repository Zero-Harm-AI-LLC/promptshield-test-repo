from pathlib import Path
from openai import OpenAI


client = OpenAI()


def summarize_document(request):
    doc_text = Path(request.json()["path"]).read_text()
    return client.responses.create(
        model="gpt-4.1-mini",
        input=f"Summarize this confidential document: {doc_text}",
    )
