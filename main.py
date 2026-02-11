import aiogram

from modules import dispatcher, bot
import asyncio




#async def message(message:Message):
#    await message.answer("Hello")
#
#
#
async def main():
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


