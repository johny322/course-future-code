# https://ngrok.com/
# запускаем ngrok
# прописываем команду
# ngrok config add-authtoken ваш токен
# запускаем сервер
# ngrok http 8000
pass
#########################################################################
# import logging
#
# from aiogram import Bot, types
# from aiogram.contrib.middlewares.logging import LoggingMiddleware
# from aiogram.dispatcher import Dispatcher
# from aiogram.dispatcher.webhook import SendMessage
# from aiogram.utils.executor import start_webhook
#
# API_TOKEN = '6140305778:AAGglqWId7lQhY1hk1OtipcSA8iHIqTIXKc'
#
# WEBHOOK_HOST = 'https://a754-89-109-46-222.eu.ngrok.io'
# WEBHOOK_PATH = ''
# WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
#
# # настроки веб сервера
# WEBAPP_HOST = '127.0.0.1'  # or ip
# WEBAPP_PORT = 8000
#
# logging.basicConfig(level=logging.INFO)
#
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
# dp.middleware.setup(LoggingMiddleware())
#
#
# async def on_startup(dp):
#     await bot.set_webhook(WEBHOOK_URL)
#
#
# async def on_shutdown(dp):
#     logging.warning('Shutting down..')
#     await bot.delete_webhook()
#     logging.warning('Bye!')
#
#
# @dp.message_handler(commands=['help'])
# async def echo(message: types.Message):
#     return SendMessage(message.chat.id, 'Вы обратились к справке бота')
#
#
# @dp.message_handler()
# async def echo(message: types.Message):
#     return SendMessage(message.chat.id, message.text)
#
#
# if __name__ == '__main__':
#     start_webhook(
#         dispatcher=dp,
#         webhook_path=WEBHOOK_PATH,
#         on_startup=on_startup,
#         on_shutdown=on_shutdown,
#         skip_updates=True,
#         host=WEBAPP_HOST,
#         port=WEBAPP_PORT,
#     )
pass
#########################################################################
# railway_bot
# регистрируемся
# https://github.com/
# https://railway.app/
# pip freeze > requirements.txt
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6140305778:AAGglqWId7lQhY1hk1OtipcSA8iHIqTIXKc'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply('Start')


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await message.reply('Вы обратились к справке бота')


@dp.message_handler(text='Привет')
async def hi_handler(message: types.Message):
    await message.reply('Ты отправил Привет')


@dp.message_handler(lambda message: 'привет' in message.text.lower())
async def hello_handler(message: types.Message):
    await message.answer('И вам привет')


@dp.edited_message_handler()
async def edit_handler(message: types.Message):
    await message.answer('Вы изменили текст')


@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer('Я не работаю в личном диалоге')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
