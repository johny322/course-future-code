import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.exceptions import MessageNotModified

from config import TOKEN, ADMIN_ID
from keyboards import get_simple_kb, get_simple_num_kb, get_inline_kb, get_inline_num_kb

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    await message.answer('Стартовое меню', reply_markup=get_simple_kb())


@dp.message_handler(Text(equals=['1']))
async def num1_menu_handler(message: types.Message):
    num = message.text
    await message.answer(f'Клавиатура для {num}', reply_markup=get_inline_kb())


@dp.message_handler(Text(equals=['1', '2']))
async def num_menu_handler(message: types.Message):
    num = message.text
    await message.answer(f'Клавиатура для {num}', reply_markup=get_simple_num_kb(num))


@dp.message_handler(Text(equals='Закрыть'))
async def menu_bot(message: types.Message):
    await message.answer('Клавиатура закрыта', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands='start_inline')
async def start_inline_handler(message: types.Message):
    await message.answer('Стартовое инлайн меню', reply_markup=get_inline_kb())


@dp.callback_query_handler(Text(equals=['1', '2']))
async def inline_btn_handler(call: types.CallbackQuery):
    num = call.data
    await call.message.edit_text(f'Нажата кнопка {num}', reply_markup=get_inline_num_kb(num))
    await call.answer()


@dp.callback_query_handler(text='back')
async def inline_back_handler(call: types.CallbackQuery):
    await call.message.edit_text('Вы вернулись в главное меню', reply_markup=get_inline_kb())
    await call.answer()


@dp.callback_query_handler(text='close')
async def inline_close_handler(call: types.CallbackQuery):
    await call.message.edit_text('Меню закрыто')
    # await call.message.delete()
    await call.answer()


@dp.callback_query_handler(Text(startswith='go_'))
async def go_inline_btn_handler(call: types.CallbackQuery):
    data = call.data
    num = data.split('_')[-1]
    try:
        await call.message.edit_text(f'Вы нажали вперед для кнопки {num}', reply_markup=get_inline_num_kb(num))
    except MessageNotModified:
        pass
    finally:
        await call.answer()


async def on_startup(dp: Dispatcher):
    await dp.bot.delete_my_commands()
    await dp.bot.send_message(ADMIN_ID, 'Бот запущен')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
