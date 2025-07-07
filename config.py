import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
LLM_MODEL = os.getenv('LLM_MODEL', 'openai/gpt-3.5-turbo')
SYSTEM_PROMPT = os.getenv('SYSTEM_PROMPT', 'Ты — полезный Telegram-бот-ассистент.') 