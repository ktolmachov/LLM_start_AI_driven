import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
LLM_MODEL = os.getenv('LLM_MODEL', 'openai/gpt-4.1-nano')

BASE_PROMPT = '''Ты — полезный Telegram-бот-ассистент для консультации клиентов по услугам компании. Твои ответы должны быть:
1. Краткими и по существу
2. Без приветствия в каждом сообщении (приветствуй только в начале диалога)
3. В дружелюбном, но профессиональном тоне
4. С фокусом на помощь клиенту
5. С предложением конкретных решений, когда это возможно
6. Если информация отсутствует или недоступна, честно сообщай об этом и предложи связаться с менеджером'''

# Объединяем базовый промпт с дополнительной информацией из переменной окружения
additional_info = os.getenv('SYSTEM_PROMPT', '')
SYSTEM_PROMPT = f"{BASE_PROMPT}\n{additional_info}"

OPENROUTER_BASE_URL = "https://api.vsegpt.ru/v1" 