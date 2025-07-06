import os
import openai

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

async def ask_llm(messages):
    client = openai.AsyncOpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL
    )
    response = await client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content 