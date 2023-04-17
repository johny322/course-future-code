import asyncio
import logging
from random import randint

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from config import TOKEN
from keyboards import random_keyboard, get_keyboard, callback_numbers, get_keyboard_fab

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


user_data = {}


async def update_num_text(message: types.Message, new_value: int):
    await message.edit_text(f"Укажите число: {new_value}", reply_markup=get_keyboard())


@dp.message_handler(commands="random")
async def cmd_random_handler(message: types.Message):
    await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=random_keyboard)


@dp.callback_query_handler(text="random_value")
async def send_random_value_handler(call: types.CallbackQuery):
    # await asyncio.sleep(5)
    await call.message.answer(str(randint(1, 10)))
    await call.answer(text='Спасибо тебе за использование бота', show_alert=True)


@dp.message_handler(commands="numbers")
async def cmd_numbers_handler(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer("Укажите число: 0", reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith="num_"))
async def callbacks_num_handler(call: types.CallbackQuery):
    user_value = user_data.get(call.from_user.id, 0)
    action = call.data.split("_")[1]
    if action == "incr":
        user_data[call.from_user.id] = user_value + 1
        await update_num_text(call.message, user_value + 1)
    elif action == "decr":
        user_data[call.from_user.id] = user_value - 1
        await update_num_text(call.message, user_value - 1)
    elif action == "finish":
        await call.message.edit_text(f"Итого: {user_value}")
        # await call.message.delete_reply_markup()
    await call.answer()


async def update_num_text_fab(message: types.Message, new_value: int):
    await message.edit_text(f"Укажите число: {new_value}", reply_markup=get_keyboard_fab())


@dp.message_handler(commands="numbers_fab")
async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer("Укажите число: 0", reply_markup=get_keyboard_fab())


@dp.callback_query_handler(callback_numbers.filter(action=["incr", "decr"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    user_value = user_data.get(call.from_user.id, 0)
    print(f'{callback_data=}, {call.data=}')
    action = callback_data["action"]
    if action == "incr":
        user_data[call.from_user.id] = user_value + 1
        await update_num_text_fab(call.message, user_value + 1)
    elif action == "decr":
        user_data[call.from_user.id] = user_value - 1
        await update_num_text_fab(call.message, user_value - 1)
    await call.answer()


@dp.callback_query_handler(callback_numbers.filter(action=["finish"]))
async def callbacks_num_finish_fab(call: types.CallbackQuery):
    user_value = user_data.get(call.from_user.id, 0)
    await call.message.edit_text(f"Итого: {user_value}")
    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
