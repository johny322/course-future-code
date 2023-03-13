# import requests
#
# BASE_URL = 'https://api.telegram.org/bot'
# TOKEN = '6140305778:AAFtPdPNkQPNKPB7h_3hPbuFv5gtqqX9KcE'
# admin_id = [5014092219]
# user_id = 5014092219
#
#
# res = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
# update = res['result'][-1]
# print(update)
#
#
# # banChatMember
# # group_id = -976606992
# # ban_user_id = 477733380
# # res = requests.get(f'{BASE_URL}{TOKEN}/banChatMember?chat_id={group_id}&user_id={ban_user_id}').json()
# # print(res)
#
# # res = requests.get(f'{BASE_URL}{TOKEN}/sendMessage?chat_id={user_id}&text=Привет, Админ').json()
# # print(res)
#
#
# # message_id = 293
# #
# # res = requests.get(f'{BASE_URL}{TOKEN}/editMessageText?chat_id={user_id}&message_id={message_id}&text=Привет, Супер Админ').json()
# # print(res)
#
# # text = '<b>Hi</b>'
# #
# # res = requests.get(f'{BASE_URL}{TOKEN}/sendMessage?chat_id={user_id}&text={text}&parse_mode=html').json()
# # print(res)
#
#
#
#

import asyncio
import time

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.utils.exceptions import MessageToEditNotFound
from os import getenv
from bot_tokens import BOT_TOKEN

# TOKEN = getenv('BOT_TOKEN')


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


# @dp.message_handler(commands=['start'])
# async def start_handler(message: types.Message):
#     chat_id = message.from_user.id
#     await bot.send_message(chat_id, 'Ты отправил start')
#
#
# @dp.message_handler(commands=['test1'])
# async def test1_handler(message: types.Message):
#     chat_id = message.from_user.id
#     await bot.send_message(chat_id, 'test1')
#
#
# async def test2_handler(message: types.Message):
#     chat_id = message.from_user.id
#     await bot.send_message(chat_id, 'test2')
#
#
# @dp.message_handler()
# async def echo_handler(message: types.Message):
#     print(message.text)
#
#
# async def main():
#     dp.register_message_handler(test2_handler, commands=['test2', 'test3'])
#     await dp.start_polling(bot)


# async def start_handler(message: types.Message):
#     chat_id = message.from_user.id
#     await bot.send_message(chat_id, 'Ты отправил start')
#
#
# async def test1_handler(message: types.Message):
#     chat_id = message.from_user.id
#     await bot.send_message(chat_id, 'test1')
#
#
# async def test2_handler(message: types.Message):
#     chat_id = message.from_user.id
#     await bot.send_message(chat_id, 'test2')
#
#
# async def echo_handler(message: types.Message):
#     print(message.text)
#
#
# async def main():
#     await dp.start_polling(bot)
#
#
# async def say_hi(dp):
#     dp.register_message_handler(start_handler, commands=['start'])
#     dp.register_message_handler(test1_handler, commands=['test1'])
#     dp.register_message_handler(echo_handler)
#     dp.register_message_handler(test2_handler, commands=['test2', 'test3'])
#
#     print('hi')
# if __name__ == '__main__':
#     executor.start_polling(dp, on_startup=say_hi)
#     # asyncio.run(main())

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, 'Ты отправил start')


@dp.message_handler(text='hi')
async def hi_handler(message: types.Message):
    await message.answer(text='Hello')


@dp.message_handler(commands=['post'])
async def post_handler(message: types.Message):
    group_id = -976606992
    await message.bot.send_message(chat_id=group_id, text='Это новый пост')


@dp.message_handler(commands=['edit_text'])
async def edit_text_handler(message: types.Message):
    new_message = await message.answer(text='Это старый текст')
    print(new_message)
    # time.sleep(10)
    await asyncio.sleep(5)
    await new_message.edit_text(text='Это новый текст')
    # try:
    #     await new_message.edit_text(text='Это новый текст')
    # except MessageToEditNotFound:
    #     await message.answer(text='Ты удалил это сообщение')
    print('hi')


@dp.errors_handler(exception=MessageToEditNotFound)
async def no_message_handler(update: types.Update, exception: MessageToEditNotFound):
    print(exception)
    message = update.message
    await message.reply('Ты удалил сообщение')
    return True


if __name__ == '__main__':
    executor.start_polling(dp)
# /start
# /help
