# Bot API
# https://core.telegram.org/bots/api
# https://tlgrm.ru/docs/bots/api

# /команда [необязательный] [аргумент]

# /start user1

# /start@TriviaBot
# /start@ApocalypseBot

# @BotFather


# https://api.telegram.org/bot<token>/METHOD_NAME
# https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe


# venv\Scripts\activate.bat
#

# pip install requests

# Информационные 100 - 199
# Успешные 200 - 299
# Перенаправления 300 - 399
# Клиентские ошибки 400 - 499
# Серверные ошибки 500 - 599
import asyncio
import time

import requests

# response = requests.get('https://www.google.com')
# print(response.status_code)
# # print(response.raise_for_status())
# if response.status_code == 200:
#     print(response.text)

# https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe
#
# BASE_URL = 'https://api.telegram.org/bot'
# token = '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'
# response = requests.get(f'{BASE_URL}{token}/getMe')
# res = response.json()
# print(res)
# print(res['result']['first_name'])


# @botname

# def get_updates():
#     r = requests.get(f'{BASE_URL}{token}/getUpdates')
#     print(r.json())
#     message_text = r.json()['result'][-1]['message']['text']
#     user_id = r.json()['result'][-1]['message']['from']['id']
#     print(message_text, user_id)
#
#     # https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendMessage?chat_id=2131&text=блаблабла
#     params = {
#         'chat_id': user_id,
#         'text': message_text
#     }
#     # ?chat_id={user_id}&text={message_text}
#     r = requests.get(f'{BASE_URL}{token}/sendMessage', params)
#     print(r.url)
#     print(r.json())
#
#
# get_updates()
#
# aiogram
# pip install aiogram

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BASE_URL = 'https://api.telegram.org/bot'
token = '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'

bot = Bot(token=token)

dp = Dispatcher(bot)


# @dp.message_handler(commands=['start'])
@dp.message_handler(text='Привет')
async def start_handler(message: types.Message):
    await message.answer(
        text='Привет. Рад с тобой общаться'
    )


# @dp.message_handler()
async def echo(message: types.Message):
    print(message.text)
    await message.reply(
        text=message.text
    )
    # print('заснул')
    # # time.sleep(10)
    # await asyncio.sleep(10)
    # print('проснулся')
    # await bot.send_message(
    #     chat_id=message.from_user.id,
    #     text=message.text
    # )


if __name__ == '__main__':
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(echo)

    executor.start_polling(dp)
