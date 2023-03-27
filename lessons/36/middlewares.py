from typing import Callable, Dict, Any, Awaitable

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types.base import TelegramObject

from config import block_users
from db_commands import get_user_from_db


class SomeMiddleware(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        print('on_pre_process_update')
        data['middleware_data'] = 'some update data'
        if update.message:
            await update.message.answer('on_pre_process_update')

    async def on_process_update(self, update: types.Update, data: dict):
        print(f'on_process_update, {data=}')

    async def on_pre_process_message(self, message: types.Message, data: dict):
        print(f'on_pre_process_message, {data=}')
        data['middleware_data1'] = 'some message data1'
        user_id = str(message.from_user.id)
        print(user_id, user_id in block_users)
        data['is_blocked'] = user_id in block_users
        # if user_id in block_users:
        #     await message.answer('ты в бане')
        #     raise CancelHandler()

    async def on_process_message(self, message: types.Message, data: dict):
        print(f'on_process_message, {data=}')
        data['middleware_data2'] = 'some message data2'
        user_id = str(message.from_user.id)
        data['user_id'] = user_id
        data['user'] = get_user_from_db(user_id)

    async def on_post_process_message(self, message: types.Message, data_from_handler: list, data: dict):
        print(f'on_post_process_message, {data=}, {data_from_handler=}')
        data['middleware_data3'] = 'some message data3'
