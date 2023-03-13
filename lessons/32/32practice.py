# import json
#
# import requests
# # pip install python-dotenv
# from dotenv import load_dotenv
# from os import getenv
#
# load_dotenv()
#
# # TOKEN = '6140305778:AAFdjoX7UB7ewHDT0cEPCjHIEy03XwQdq24'
# TOKEN = getenv('TOKEN')
#
# prefix = 'https://api.telegram.org/bot'
#
# geturl = prefix + TOKEN + '/getUpdates'
# sendurl = prefix + TOKEN + '/sendMessage'
# timeout = 60
#
#
# # offset = 0
# # dt = dict(offset=offset, timeout=timeout)
# # req = requests.post(geturl, data=dt).json()
# # print(req)
#
#
# def main():
#     offset = 549804962 + 1
#     while True:
#         dt = dict(offset=offset, timeout=timeout)
#         try:
#             req = requests.post(geturl, data=dt).json()
#         except ValueError:
#             continue
#         if not req['ok'] or not req['result']:
#             continue
#         for update in req['result']:
#             print(f'{update=}')
#
#             if 'message' in update:
#                 message = update['message']
#                 id = message['chat']['id']
#
#                 if 'text' in message:
#                     inline_keyboard = [
#                         [
#                             {'text': 'Да', 'callback_data': 'yes'},
#                             {'text': 'Нет', 'callback_data': 'no'}
#                         ],
#                         [
#                             {'text': 'Google', 'url': 'www.google.ru'}
#                         ]
#                     ]
#                     keyboard = json.dumps(
#                         {'inline_keyboard': inline_keyboard}
#                     )
#
#                     dt = dict(chat_id=id, text='Инлайн клавиатура', reply_markup=keyboard)
#                     print(f'{dt=}')
#
#                     print(requests.post(sendurl, data=dt).json())
#             elif 'callback_query' in update:
#                 callback_query = update['callback_query']
#                 id = callback_query['from']['id']
#                 if callback_query['data'] == 'yes':
#                     text = 'Вы нажали на ДА'
#                 else:
#                     text = 'Вы нажали на НЕТ'
#                 dt = dict(chat_id=id, text=text)
#                 print(f'{dt=}')
#                 print(requests.post(sendurl, data=dt).json())
#
#             offset = update['update_id'] + 1
#
#
# if __name__ == '__main__':
#     main()


# # https://docs.aiogram.dev/en/latest/
#
# import logging
#
# from aiogram import Bot, Dispatcher, executor, types
# # pip install python-dotenv
# from dotenv import load_dotenv
# from os import getenv
#
# load_dotenv()
#
# API_TOKEN = getenv('TOKEN')
#
# logging.basicConfig(level=logging.INFO)
#
# proxy_url = 'http://proxy.server:3128'
# # proxy_url = None
# bot = Bot(token=API_TOKEN, proxy=proxy_url)
# dp = Dispatcher(bot)
#
#
# @dp.message_handler(commands=['start'])
# async def start_handler(message: types.Message):
#     await message.answer('Вы ввели команду /start')
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)

#
# https://docs.aiogram.dev/en/latest/examples/webhook_example.html
import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

API_TOKEN = 'Ваш  токен'

# webhook settings
WEBHOOK_HOST = 'адрес сайта'
WEBHOOK_PATH = '/path/to/api'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = 'localhost'  # or ip
WEBAPP_PORT = 3001

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    # insert code here to run it after start


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning('Bye!')


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
