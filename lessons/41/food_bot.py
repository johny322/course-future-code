import asyncio
import logging
from aiogram import types
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import BotCommandScopeDefault, BotCommand

from config import TOKEN
from filters import AdminFilter
from keyboards import main_menu, menu_pizza_kb, pizza_callback, back_callback

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


async def set_default_commands(bot: Bot):
    return await bot.set_my_commands(
        commands=[
            BotCommand('menu', 'Вывести меню'),
            BotCommand('help', 'Помощь'),
            BotCommand('support', 'Поддержка'),
        ],
        scope=BotCommandScopeDefault(),

    )


@dp.message_handler(AdminFilter(), CommandStart())
async def admin_start(message: types.Message):
    await message.reply('Команды установлены')
    await set_default_commands(message.bot)


@dp.message_handler(commands="menu")
async def menu_handler(message: types.Message):
    await message.answer('Выбери из меню', reply_markup=main_menu())


@dp.callback_query_handler(text="pizza_cat")
async def pizza_cat_handler(call: types.CallbackQuery):
    await call.message.edit_text(
        text='Выбери пиццу',
        reply_markup=menu_pizza_kb(['4 сыра', 'маргарита'])
    )
    await call.answer()


@dp.callback_query_handler(pizza_callback.filter())
async def pizza_handler(call: types.CallbackQuery, callback_data: dict):
    await call.message.edit_text(f'Вы заказали пиццу {callback_data["name"]}')
    await call.answer(text='Спасибо за заказ')


@dp.callback_query_handler(back_callback.filter())
async def back_handler(call: types.CallbackQuery, callback_data: dict):
    menu = callback_data['menu']
    if menu == 'start':
        await call.message.edit_text('Выбери из меню', reply_markup=main_menu())
    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
