import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Я минимальный Telegram-бот.")

@dp.message()
async def echo_message(message: Message):
    await message.answer("Вы написали: " + message.text)

async def start_bot():
    await dp.start_polling(bot) 