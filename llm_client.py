import openai
from config import OPENROUTER_API_KEY, LLM_MODEL, SYSTEM_PROMPT
import logging

openai.api_key = OPENROUTER_API_KEY
openai.base_url = "https://openrouter.ai/api/v1"

logging.basicConfig(level=logging.INFO, filename='logs\\bot.log')

def build_messages(user_messages):
    return [{"role": "system", "content": SYSTEM_PROMPT}] + user_messages

async def ask_llm(user_messages):
    messages = build_messages(user_messages)
    logging.info('LLM request: %s', messages)
    response = await openai.ChatCompletion.acreate(
        model=LLM_MODEL,
        messages=messages,
    )
    logging.info('LLM response: %s', response)
    return response.choices[0].message.content 