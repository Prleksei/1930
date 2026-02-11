from aiogram.filters import Command, CommandStart
from .settings import dispatcher, bot
from aiogram.types import Message

@dispatcher.message(CommandStart())
async def command_handler(message:Message):
    await message.answer(text = "Hello")
