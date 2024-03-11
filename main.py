from cgitb import handler
import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from core.handlers.handler import router

load_dotenv()

TOKEN = os.getenv("TOKEN")


async def main():
    bot = Bot(token=TOKEN) # type: ignore
    dp = Dispatcher()
    dp.include_routers(router)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stoped!")
