import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from config import TOKEN
from keyboards import reply_keyboard, ReplyKeyboardRemove, inline_kb1, inline_kb_full, many_data_keyboard

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def start_command_handler(message: types.Message):
    await message.answer('Привет', reply_markup=inline_kb_full)


@dp.message_handler(commands='rm')
async def rm_keyboard_handler(message: types.Message):
    await message.answer('Клавиатура была удалена', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands='many')
async def many_keyboard_handler(message: types.Message):
    await message.answer('Клавиатура', reply_markup=many_data_keyboard('key', '1', '2', 'some text'))


@dp.callback_query_handler(Text(startswith='btn'))
async def btns_callback_queries_handler(callback_query: types.CallbackQuery):
    data = callback_query.data
    btn_num = int(data.replace('btn', ''))
    await callback_query.answer(text=f'ты нажал на кнопку {btn_num}', show_alert=True)


@dp.callback_query_handler(Text(startswith='key'))
async def many_callback_queries_handler(callback_query: types.CallbackQuery):
    data = callback_query.data
    print(data)
    args = data.split(':')
    print(args)
    last_arg = args[-1]
    await callback_query.answer(text=last_arg)


@dp.callback_query_handler(text='btn2')
async def btn2_callback_queries_handler(callback_query: types.CallbackQuery):
    await callback_query.answer(text='ты нажал на кнопку 2', show_alert=True)


@dp.callback_query_handler()
async def all_callback_queries_handler(callback_query: types.CallbackQuery):
    # print(callback_query)
    # await callback_query.message.answer(f'Ответ на callback_query с {callback_query.data=}')
    await bot.answer_callback_query(callback_query.id)
    # await callback_query.answer(text='ты нажал на кнопку', show_alert=True)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
