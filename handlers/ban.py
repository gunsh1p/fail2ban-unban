from aiogram import Dispatcher
from aiogram.types import Message

from utils.args import parse_args

async def ban(message: Message):
    args = parse_args(message.get_args())
    if len(args) == 0:
        await message.reply("Hello, admin! This command bans an ip or a range")
    else:
        pass


def register_ban(dp: Dispatcher):
    dp.register_message_handler(ban, commands=["ban"], state="*", is_admin=True)