import typing

from aiogram.dispatcher.filters import BoundFilter

class IsAdmin(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin: typing.Optional[bool] = None):
        self.is_admin = is_admin

    async def check(self, obj):
        if self.is_admin is None:
            return False
        config = obj.bot.get('config')
        return (obj.from_user.id in config["admins"]) == self.is_admin
