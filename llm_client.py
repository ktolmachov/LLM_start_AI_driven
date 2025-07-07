import openai
from openai import AsyncOpenAI
from config import OPENROUTER_API_KEY, LLM_MODEL, SYSTEM_PROMPT, OPENROUTER_BASE_URL
from logger import log_message

client = AsyncOpenAI(api_key=OPENROUTER_API_KEY, base_url=OPENROUTER_BASE_URL)


def build_messages(user_messages):
    return [{"role": "system", "content": SYSTEM_PROMPT}] + user_messages

async def ask_llm(user_messages, user_id=None):
    messages = build_messages(user_messages)
    log_message(user_id or "system", "llm_request", str(messages))
    response = await client.chat.completions.create(
        model=LLM_MODEL,
        messages=messages,
    )
    log_message(user_id or "system", "llm_response", str(response))
    return response.choices[0].message.content 