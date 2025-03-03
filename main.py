import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InputFile
import aiohttp
import asyncio
from datetime import datetime, timedelta
import config
from aiogram.types import FSInputFile


TOKEN = config.TOKEN
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

kb1 = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Расписание")],
        [KeyboardButton(text="Новости"), 
         KeyboardButton(text="Посвящение в лицеисты 1488")],
    ])

@dp.message(Command(commands=["start"]))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я оффициальный бот лицея инновационных технологий. \n Чем я могу Вам помочь?",
        reply_markup=kb1
    )
@dp.message(lambda message: message.text in ["Расписание", "Новости", "Посвящение в лицеисты 1488"])
async def weather_buttons(message: Message):
    await message.answer_photo(photo=FSInputFile('hent.jpg', filename='Снеговик'), caption='Это снеговик!')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
