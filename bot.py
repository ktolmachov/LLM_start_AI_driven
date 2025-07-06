import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from llm_client import ask_llm
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Я минимальный Telegram-бот.")

@dp.message()
async def handle_message(message: Message):
    messages = [
        {"role": "system", "content": "Вы — помощник."},
        {"role": "user", "content": message.text}
    ]
    #reply = await ask_llm(messages)
    #await message.answer(reply)
    await message.answer("Временно без ответа от LLM.")

async def start_bot():
    try:
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        print("Polling was cancelled. Shutting down gracefully.")
    except Exception as e:
        print(f"Unhandled error during polling: {e}")

if __name__ == "__main__":
    asyncio.run(start_bot())