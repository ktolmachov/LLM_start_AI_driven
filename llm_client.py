import openai
from config import OPENROUTER_API_KEY, LLM_MODEL, SYSTEM_PROMPT
from logger import log_message

openai.api_key = OPENROUTER_API_KEY
openai.base_url = "https://openrouter.ai/api/v1"


def build_messages(user_messages):
    return [{"role": "system", "content": SYSTEM_PROMPT}] + user_messages

async def ask_llm(user_messages, user_id=None):
    messages = build_messages(user_messages)
    log_message(user_id or "system", "llm_request", str(messages))
    response = await openai.ChatCompletion.acreate(
        model=LLM_MODEL,
        messages=messages,
    )
    log_message(user_id or "system", "llm_response", str(response))
    return response.choices[0].message.content 