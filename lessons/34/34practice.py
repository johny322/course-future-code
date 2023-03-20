
# import logging
# import os
#
# from aiogram import Bot, Dispatcher, executor, types
#
# TOKEN = os.environ.get('TOKEN')
# API_TOKEN = TOKEN
#
# logging.basicConfig(level=logging.INFO)
#
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
#
#
# @dp.message_handler(commands=['start'])
# async def start_handler(message: types.Message):
#     await message.answer("Привет! Вы ввели /start.")
#
#
# @dp.message_handler()
# async def echo_handler(message: types.Message):
#     await message.answer(message.text)
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)

# pass
# import logging
# import os
#
# from aiogram import Bot, types
# from aiogram.contrib.middlewares.logging import LoggingMiddleware
# from aiogram.dispatcher import Dispatcher
# from aiogram.dispatcher.webhook import SendMessage
# from aiogram.utils.executor import start_webhook
#
# API_TOKEN = os.environ.get('TOKEN')
#
# WEBHOOK_HOST = 'https://my-bot-container-ryavg.run-eu-central1.goorm.site'
# WEBHOOK_PATH = ''
# WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
#
# WEBAPP_HOST = '0.0.0.0'  # or ip
# WEBAPP_PORT = 80
#
# logging.basicConfig(level=logging.INFO)
#
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
# dp.middleware.setup(LoggingMiddleware())
#
#
# @dp.message_handler(commands=['start'])
# async def start_handler(message):
#     await message.answer('start')
#
#
# @dp.message_handler()
# async def echo_handler(message: types.Message):
#     await bot.send_message(message.chat.id, message.text)
#     # return SendMessage(message.chat.id, message.text)
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
from sqlite3.dbapi2 import IntegrityError


# import os
# import sqlite3
#
# db_filename = 'test.db'
# db_is_new = not os.path.exists(db_filename)
# conn = sqlite3.connect(db_filename)
# if db_is_new:
#     print('Создана новая база')
# else:
#     print('База данных уже существует.')
# conn.close()

# import sqlite3
#
# db_filename = 'test.db'
# conn = sqlite3.connect(db_filename)
# conn.close()

# import os
# import sqlite3
#
# db_filename = 'test.db'
# schema_filename = 'todo_schema.sql'
# db_is_new = not os.path.exists(db_filename)
# with sqlite3.connect(db_filename) as conn:
#     if db_is_new:
#         print('Создание таблиц')
#         with open(schema_filename, 'r') as f:
#             schema = f.read()
#         conn.executescript(schema)
#         print('Добавление данных')
#         conn.executescript("""
#        insert into project (name, description, deadline)
#        values ('project1', 'Python Module1 of the Week',
#        '2022-11-01');
#        insert into project (name, description, deadline)
#        values ('project2', 'Python Module2 of the Week',
#        '2022-11-01');
#
#        """)
#     else:
#         print('База уже создана')

import sqlite3

import logging
import os

from aiogram import Bot, Dispatcher, executor, types

TOKEN = os.environ.get('TOKEN')
API_TOKEN = TOKEN

logging.basicConfig(level=logging.INFO)


def create_table():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
               userid INT PRIMARY KEY,
               username TEXT);
               """)
    conn.commit()
    cur.close()
    conn.close()


def check_user_exist(user_id):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM users WHERE userid = {user_id}""")
    user = cur.fetchone()
    # print(user)
    cur.close()
    conn.close()
    return user


def add_user(user_id, username):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("""INSERT INTO users(userid, username) VALUES (?,?)""", (user_id, username))
    conn.commit()
    cur.close()
    conn.close()


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    result = check_user_exist(user_id)
    if result is None:
        username = message.from_user.username
        add_user(user_id, username)

    await message.answer("Привет! Вы ввели /start.")


@dp.message_handler(commands=['db'])
async def dp_handler(message: types.Message):
    user_id = message.from_user.id
    result = check_user_exist(user_id)
    if result is not None:
        await message.answer('Вы есть в базе данных')
    else:
        await message.answer('Вас нет в базе данных')


@dp.message_handler(text='запиши в бд')
async def add_user_handler(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    try:
        add_user(user_id, username)
        await message.answer('Вы были добавлены в бд')
    except IntegrityError:
        await message.answer('Вы уже есть в бд')


@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(message.text)


async def on_startup(dp):
    create_table()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
