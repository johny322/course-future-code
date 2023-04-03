import logging
import sqlite3

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import CommandStart

from config import TOKEN, DB_NAME
from database import Database

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

db = Database(DB_NAME)


async def on_startup(dp):
    try:
        db.create_table_users()
        print('Таблица создана')
    except Exception as e:
        print(e)


@dp.message_handler(CommandStart())
async def bot_start_handler(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        # print(err)
        pass
    count_users = db.count_users()[0]
    await message.answer(
        '\n'.join([
            f'Привет, {name}!',
            'Ты был занесен в базу данных',
            f'В базе данных {count_users} пользователей'
        ])
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
