import logging
import random
import re

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from config import TOKEN, ADMIN_ID
from keyboards import start_menu, main_game_menu

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

user_data = {}


def random_num():
    secret_number = random.randint(1, 10)
    return secret_number


@dp.message_handler(commands=['start'])
async def main_start_handler(message: types.Message):
    await message.answer(
        'Привет! Это игровой бот!\nДля старта выбери игру',
        reply_markup=main_game_menu()
    )


@dp.message_handler(text=['Игра случайное число'])
async def start_random_num_game_handler(message: types.Message):
    await message.answer(
        'Привет! Это игра угадай число!\nДля старта игры нажми на кнопку начать',
        reply_markup=start_menu()
    )


@dp.callback_query_handler(Text(equals='cancel'))
async def end_game_handler(call: types.CallbackQuery):
    await call.message.delete()
    await call.answer()


@dp.callback_query_handler(Text(equals='startgame'))
async def start_game_handler(call: types.CallbackQuery):
    secret_number = random_num()
    user_data[call.from_user.id] = dict(
        secret_number=secret_number,
        attempts=3
    )
    await call.message.answer('Я загадал число от 1 до 10\nПопробуй угадай его')
    await bot.answer_callback_query(call.id)
    await call.message.delete()
    print(secret_number)


@dp.message_handler(regexp=re.compile(r'^\d+$'))
async def check_numbers_handler(message: types.Message):
    user_number = int(message.text)

    current_user_data = user_data.get(message.from_user.id)
    if current_user_data is None:
        await message.reply('Для начала игры введите /start')
        return

    secret_number = current_user_data.get('secret_number')
    attempts = current_user_data.get('attempts', 0)

    if secret_number is not None:
        attempts -= 1
        current_user_data['attempts'] = attempts
        if user_number > secret_number:
            await message.reply(f'Секретное число меньше.\nКоличество попыток: {attempts}')
        elif user_number < secret_number:
            await message.reply(f'Секретное число больше.\nКоличество попыток: {attempts}')
        else:
            await message.reply('Вы угадали!\nНачать заново?', reply_markup=start_menu())
            user_data[message.from_user.id] = dict(
                secret_number=None,
                attempts=None
            )
            return

        if attempts < 1:
            await message.reply('Вы проиграли', reply_markup=start_menu())
            user_data[message.from_user.id] = dict(
                secret_number=None,
                attempts=None
            )

    else:
        await message.reply('Для начала игры введите /start')


async def on_startup(dp: Dispatcher):
    await dp.bot.delete_my_commands()
    await dp.bot.send_message(ADMIN_ID, 'Бот запущен')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
