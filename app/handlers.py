from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router, F

router_one  = Router()


@router_one.message(CommandStart(deep_link=True, magic=F.args.isdigit()))
async def cmd_start(message: Message, command: CommandStart):
    await message.answer(f'Привет! command.args = {command.args}')

@router_one.message(F.photo)
async def comeEcho(message: Message):
    await message.answer(f'ID Photo: {message.photo[-1].file_id}')