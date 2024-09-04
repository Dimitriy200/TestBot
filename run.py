import asyncio
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart



load_dotenv()
bot = Bot(token = os.getenv('TOKEN'))
dispatcher = Dispatcher()


@dispatcher.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')

@dispatcher.message()
async def comeEcho(message: Message):
    await message.answer('Неизвестная комманда')


async def main():
    await dispatcher.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('BOT HAS BEEN STOPED')