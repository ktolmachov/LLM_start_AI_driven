import os
import asyncio
import time
from datetime import datetime, timedelta
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from llm_client import ask_llm
from config import TELEGRAM_TOKEN, SYSTEM_PROMPT
from logger import log_message

if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN must be set in environment variables")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

# История сообщений: user_id -> (timestamp, list of dict(role, content))
user_histories = {}

# Константа для времени хранения истории (3 дня в секундах)
HISTORY_TTL = 3 * 24 * 60 * 60  # 3 дня в секундах

async def cleanup_old_histories():
    """Очищает истории диалогов старше 3 дней"""
    while True:
        current_time = time.time()
        # Создаем список ключей, которые нужно удалить
        to_delete = []
        for user_id, (timestamp, _) in user_histories.items():
            if current_time - timestamp > HISTORY_TTL:
                to_delete.append(user_id)
        
        # Удаляем старые истории
        for user_id in to_delete:
            del user_histories[user_id]
            log_message(user_id, "system", "История диалога удалена по истечении срока хранения")
        
        # Ждем час перед следующей проверкой
        await asyncio.sleep(3600)  # 1 час

@dp.message(Command("start"))
async def cmd_start(message: Message):
    if not message.from_user:
        return
    user_histories[message.from_user.id] = (
        time.time(),  # текущий timestamp
        [{"role": "system", "content": SYSTEM_PROMPT}]
    )
    await message.answer("Привет! Я бот-консультант. Задавай вопросы об услугах компании.")

@dp.message()
async def handle_message(message: Message):
    if not message.from_user:
        return
    user_id = message.from_user.id
    current_time = time.time()
    
    if user_id not in user_histories:
        # Инициализируем историю только с системным промптом
        user_histories[user_id] = (
            current_time,
            [{"role": "system", "content": SYSTEM_PROMPT}]
        )
        # Добавляем приветственное сообщение в историю
        welcome_message = "Привет! Я бот-консультант. Задавай вопросы об услугах компании."
        user_histories[user_id][1].append({"role": "assistant", "content": welcome_message})
        await message.answer(welcome_message)
        return

    if not message.text:
        await message.answer("Извините, я могу обрабатывать только текстовые сообщения.")
        return

    # Обновляем timestamp и добавляем сообщение пользователя
    timestamp, history = user_histories[user_id]
    user_histories[user_id] = (current_time, history)
    history.append({"role": "user", "content": message.text})
    log_message(user_id, "user", message.text)
    
    # Отправляем всю историю в LLM
    reply = await ask_llm(history)
    if not reply:
        await message.answer("Извините, произошла ошибка при генерации ответа.")
        return
    
    # Добавляем ответ ассистента в историю
    history.append({"role": "assistant", "content": reply})
    log_message(user_id, "assistant", reply)
    await message.answer(reply)

async def start_bot():
    try:
        # Запускаем задачу очистки старых историй
        asyncio.create_task(cleanup_old_histories())
        # Запускаем бота
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        print("Polling was cancelled. Shutting down gracefully.")
    except Exception as e:
        print(f"Unhandled error during polling: {e}")

if __name__ == "__main__":
    asyncio.run(start_bot())