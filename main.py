import aiogram
from aiogram import Dispatcher, Bot
from aiogram.types import Message
import asyncio


TOKEN = "8283782074:AAETAJV9UTjIEpKQ_KuoEzO2IDANwl9owZs"
bot = Bot("")
dispatcher = Dispatcher(bot)

async def message(message:Message):
    await message.answer("Hello")

async def main():
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


