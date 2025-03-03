from config import TOKEN

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import aiohttp
import asyncio
from datetime import datetime, timedelta
import config


TOKEN = config.BOT_TOKEN
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def cmd_start(message: Message):
    await message.reply(
        "Привет! Я - официальный бот Лицея Инновационных Технологий г. Хабаровска\n\nЧем я могу тебе помочь?"
    )

async def main():    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())