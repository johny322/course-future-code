import logging
from typing import List

from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Command
from aiogram.types import BotCommandScopeChat, BotCommand

from config import TOKEN, GROUP_ID
from bot_commands import set_default_commands, force_reset_all_commands, set_starting_commands, set_chat_admins_commands
from filters import IsGroup, AdminFilter, IsPrivate, MyChatIDFilter

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


async def on_startup(dp: Dispatcher):
    await set_default_commands(bot)


@dp.message_handler(IsPrivate(), commands='start')
async def start_command(message: types.Message):
    await message.answer('Привет!')
    # await set_default_commands(bot)
    # await set_starting_commands(message.bot, message.from_user.id)


@dp.message_handler(commands=['get_commands'])
async def message_get_command(message: types.Message):
    no_lang = await message.bot.get_my_commands(scope=BotCommandScopeChat(message.from_user.id))
    no_args = await message.bot.get_my_commands()
    ru_lang: List[BotCommand] = await message.bot.get_my_commands(scope=BotCommandScopeChat(message.from_user.id),
                                                                  language_code='ru')
    print(no_lang, no_args, ru_lang)


@dp.message_handler(commands=['reset_commands'])
async def message_get_command(message: types.Message):
    # await force_reset_all_commands(message.bot, message.from_user.id)
    # await message.answer('Команды успешно удалены')
    await message.bot.delete_my_commands()


@dp.message_handler(IsGroup(), Command('set_description', prefixes='!/'), AdminFilter())
async def set_new_description_handler(message: types.Message):
    source_message = message.reply_to_message
    description = source_message.text
    print(description)
    await message.chat.set_description(description=description)


@dp.message_handler(IsPrivate(), commands=['private'])
async def private_chat_handler(message: types.Message):
    await message.answer('Это приватный чат')


@dp.message_handler(IsGroup(), commands=['group'])
async def private_chat_handler(message: types.Message):
    await message.answer('Это групповой чат')


@dp.message_handler(MyChatIDFilter(123), commands=['admin'])
async def id_filter_handler(message: types.Message):
    await message.answer('ты избран')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
