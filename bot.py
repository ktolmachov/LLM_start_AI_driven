import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from llm_client import ask_llm
from config import TELEGRAM_TOKEN, SYSTEM_PROMPT
from logger import log_message

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

# История сообщений: user_id -> list of dict(role, content)
user_histories = {}

@dp.message(Command("start"))
async def cmd_start(message: Message):
    user_histories[message.from_user.id] = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    await message.answer("Привет! Я бот-консультант. Задавай вопросы об услугах компании.")

@dp.message()
async def handle_message(message: Message):
    user_id = message.from_user.id
    if user_id not in user_histories:
        user_histories[user_id] = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
    # Добавляем сообщение пользователя
    user_histories[user_id].append({"role": "user", "content": message.text})
    log_message(user_id, "user", message.text)
    # Отправляем всю историю в LLM
    reply = await ask_llm(user_histories[user_id])
    # Добавляем ответ ассистента в историю
    user_histories[user_id].append({"role": "assistant", "content": reply})
    log_message(user_id, "assistant", reply)
    await message.answer(reply)

async def start_bot():
    try:
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        print("Polling was cancelled. Shutting down gracefully.")
    except Exception as e:
        print(f"Unhandled error during polling: {e}")

if __name__ == "__main__":
    asyncio.run(start_bot())