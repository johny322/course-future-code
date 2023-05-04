import handlers
from aiogram import Dispatcher, executor, types

from loader import dp


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        types.BotCommand('set_photo', 'Установить фото в группе'),
        types.BotCommand('set_title', 'Установить название группы'),
        types.BotCommand('set_description', 'Установить описание группы'),
        types.BotCommand('ro', 'Режим Read Only'),
        types.BotCommand('unro', 'Отключить RO'),
        types.BotCommand('ban', 'Забанить пользователя'),
        types.BotCommand('unban', 'Разбанить пользователя'),
    ])


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
