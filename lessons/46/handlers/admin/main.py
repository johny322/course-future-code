from aiogram import types

from loader import dp
from config import ADMINS, channels
from keyboards import post_callback


@dp.callback_query_handler(post_callback.filter(action='post'), user_id=ADMINS)
async def approve_post(call: types.CallbackQuery):
    await call.answer('Вы одобрили этот пост', show_alert=True)
    target_channel = channels[0]
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=target_channel)


@dp.callback_query_handler(post_callback.filter(action='cancel'), user_id=ADMINS)
async def decline_post(call: types.CallbackQuery):
    await call.answer('Вы отклонили этот пост', show_alert=True)
    await call.message.edit_reply_markup()
