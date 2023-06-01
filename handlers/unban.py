from aiogram import Dispatcher
from aiogram.types import Message


async def unban(message: Message):
    await message.reply("Hello, admin! This command unbans an ip or a range")


def register_unban(dp: Dispatcher):
    dp.register_message_handler(unban, commands=["unban"], state="*", is_admin=True)