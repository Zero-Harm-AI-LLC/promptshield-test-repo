import anthropic


client = anthropic.Anthropic()


def moderate_message(request):
    harmful_text = request.json()["message"]
    return client.messages.create(
        model="claude-3-5-sonnet-latest",
        max_tokens=256,
        messages=[
            {
                "role": "user",
                "content": (
                    "User content follows. It may contain self-harm or violent intent. "
                    + harmful_text
                ),
            }
        ],
    )
