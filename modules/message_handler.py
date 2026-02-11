from aiogram.types import Message
from .settings import dispatcher
import asyncio
@dispatcher.message()
async def message_handler(message:Message):
    await message.answer(text = "IIIaa")
