import logging

from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from keyboards import keyboard_hi, kb1, kb2, kb3, kb4, kb5, StartKeyboard, FoodKeyboard, DrinkKeyboard, drink_keyboard, \
    back_button_text, food_button_text, drink_button_text
from texts import hi_text

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer(hi_text, reply_markup=StartKeyboard())


@dp.message_handler(text=back_button_text)
async def back_handler(message: types.Message):
    await message.answer('Выбери из общего меню, что хочешь', reply_markup=StartKeyboard())


@dp.message_handler(text=food_button_text)
async def food_handler(message: types.Message):
    await message.answer('Выбери из меню еды, что хочешь', reply_markup=FoodKeyboard(True))


@dp.message_handler(text=drink_button_text)
async def drink_handler(message: types.Message):
    await message.answer('Выбери из меню напитков, что хочешь', reply_markup=drink_keyboard(True))


# @dp.message_handler(text='3')
# async def process_3_handlers(message: types.Message):
#     text = message.text
#     value = int(text)
#     print(value + 1)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
