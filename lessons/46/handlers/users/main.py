from typing import Union

from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from filters import IsChannel
from loader import dp, bot
from config import channels, ADMINS
from keyboards import check_button, confirmation_keyboard, post_callback
from states import NewPost


@dp.message_handler(Command("channels"))
async def show_channels(message: types.Message):
    channels_format = str()
    for channel in channels:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        channels_format += f'Канал <a href="{invite_link}">{chat.title}</a>\n\n'
    await message.answer(f'Вам необходимо подписаться на следующие каналы: \n'
                         f'{channels_format}',
                         reply_markup=check_button,
                         disable_web_page_preview=True)


async def check(user_id, channel: Union[int, str]):
    bot = Bot.get_current()
    member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
    return member.is_chat_member()


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    result = str()
    for channel in channels:
        status = await check(user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f'Подписка на канал {channel.title} оформлена!'
        else:
            invite_link = await channel.export_invite_link()
            result += (f'Подписка на канал {channel.title} не оформлена!'
                       f'<a href="{invite_link}">Нужно  подписаться.</a>\n\n')
    await call.message.answer(result, disable_web_page_preview=False)
    await call.answer()


@dp.message_handler(Command("create_post"))
async def create_post(message: types.Message):
    await message.answer("Отправьте мне пост для публикации")
    await NewPost.EnterMessage.set()


@dp.message_handler(state=NewPost.EnterMessage)
async def enter_message(message: types.Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer('Вы собираетесь отправить пост на проверку?', reply_markup=confirmation_keyboard)
    await NewPost.Confirm.set()


@dp.callback_query_handler(post_callback.filter(action='post'), state=NewPost.Confirm)
async def confirm_post(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        mention = data.get("mention")
    await state.finish()
    await call.message.delete_reply_markup()
    await call.message.answer("Вы отправили текст на проверку")
    admin_id = ADMINS[0]
    await bot.send_message(chat_id=admin_id, text=f'Пользователь {mention} хочет сделать пост:')
    await bot.send_message(chat_id=admin_id, text=text, parse_mode="HTML", reply_markup=confirmation_keyboard)


@dp.callback_query_handler(post_callback.filter(action='cancel'), state=NewPost.Confirm)
async def cancel_post(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer('Вы отклонили пост')


@dp.message_handler(state=NewPost.Confirm)
async def _post_unknown(message: types.Message):
    await message.answer('Выберите или опубликовать или отклонить текст')


@dp.message_handler(IsChannel(), content_types=types.ContentType.ANY)
async def get_channel_info(message: types.Message):
    await message.answer(f'Сообщение прислано с канала {message.forward_from_chat.title}. \n'
                         f'Username: @{message.forward_from_chat.username}. \n'
                         f'ID: {message.forward_from_chat.id}')
