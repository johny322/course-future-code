from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import ReplyKeyboardRemove

from loader import dp


@dp.message_handler(CommandStart())
async def start_handler(message: types.Message):
    await message.answer('Привет', reply_markup=ReplyKeyboardRemove())
