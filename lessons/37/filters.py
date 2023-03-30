from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class AdminFilter(BoundFilter):
    async def check(self, message: types.Message):
        member = await message.chat.get_member(message.from_user.id)
        return member.is_chat_admin()


class IsGroup(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP,
        )


class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE


class MyChatIDFilter(BoundFilter):
    def __init__(self, chat_id: int):
        self.chat_id = chat_id
        print(f'{self.chat_id=}')

    async def check(self, message: types.Message):
        res = message.from_user.id == self.chat_id
        print(f'{res}')
        return res
