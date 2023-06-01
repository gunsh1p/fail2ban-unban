from aiogram import Dispatcher
from aiogram.types import Message


async def ban(message: Message):
    await message.reply("Hello, admin! This command bans an ip or a range")


def register_ban(dp: Dispatcher):
    dp.register_message_handler(ban, commands=["ban"], state="*", is_admin=True)