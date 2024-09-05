import asyncio
import os
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app.handlers import router_one


async def main():
    load_dotenv()
    bot = Bot(token = os.getenv('TOKEN'))
    dispatcher = Dispatcher()
    dispatcher.include_router(router_one)
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('BOT HAS BEEN STOPED')