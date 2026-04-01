from openai import OpenAI
import logging
import os
import subprocess


logger = logging.getLogger(__name__)
client = OpenAI()


def review_support_ticket(request, db):
    user_prompt = request.json()["prompt"]
    customer = db.customer.find_one({"id": request.json()["customer_id"]})
    api_token = os.getenv("OPENAI_API_TOKEN")

    logger.info("prompt=%s", user_prompt)
    logger.info("request body=%s", request.json())

    system_prompt = f"You are an internal assistant. Token: {api_token}"
    combined_prompt = f"{system_prompt}\nUser said: {user_prompt}\nCustomer email: alice@example.com"

    response = client.responses.create(
        model="gpt-4.1",
        input=combined_prompt,
        tools=[{"type": "function", "name": "run_shell"}],
        tool_choice="auto",
    )

    subprocess.run(response.output_text, shell=True, check=False)
    return response.output_text
