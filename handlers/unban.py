import os

from aiogram import Dispatcher
from aiogram.types import Message

from utils.args import parse_args
from utils.ipv4 import is_ipv4


async def unban(message: Message):
    args = parse_args(message.get_args())
    if len(args) == 0:
        await message.reply(f"{message.from_user.first_name}, this command unbans an ip or a range. Type /unban help for more information")
        return
    if args[0] == "help":
        await message.reply("/unban &lt;jail&gt; &lt;ip&gt;")
        return
    if len(args) < 2:
        await message.reply(f"{message.from_user.first_name}, this command unbans an ip or a range. Type /unban help for more information")
        return
    if not is_ipv4(args[1]):
        await message.reply(f"{message.from_user.first_name}, you wrote an invalid ipv4. Try another one!")
        return
    return_code = os.system(f"fail2ban-client set {args[0]} unbanip {args[1]}")
    await message.reply(f"{message.from_user.first_name}, command was executed! Return code is {return_code}")


def register_unban(dp: Dispatcher):
    dp.register_message_handler(unban, commands=["unban"], state="*", is_admin=True)