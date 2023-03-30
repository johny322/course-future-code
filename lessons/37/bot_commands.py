from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat, BotCommandScopeAllPrivateChats, \
    BotCommandScopeAllGroupChats, BotCommandScopeAllChatAdministrators, BotCommandScopeChatAdministrators


async def set_default_commands(bot: Bot):
    await bot.set_my_commands(
        commands=[
            BotCommand('start', 'Перезапустить бота'),
            BotCommand('help', 'Помощь'),
            BotCommand('set_description', 'Установить описание группы'),

        ],
        scope=BotCommandScopeDefault(),
    )


async def set_starting_commands(bot: Bot, chat_id: int):
    STARTING_COMMANDS = {
        'ru': [
            BotCommand('start', 'Начать заново'),
            BotCommand('get_commands', 'Получить список команд'),
            BotCommand('reset_commands', 'Сбросить команды'),
            BotCommand('test', 'Тест команда'),
        ],
        'en': [
            BotCommand('start', 'Restart bot'),
            BotCommand('get_commands', 'Retrieve command list'),
            BotCommand('reset_commands', 'Reset commands')
        ]
    }
    for language_code, commands in STARTING_COMMANDS.items():
        await bot.set_my_commands(
            commands=commands,
            scope=BotCommandScopeChat(chat_id),
            language_code=language_code
        )


async def force_reset_all_commands(bot: Bot, chat_id: int):
    for language_code in ('ru', 'en'):
        for scope in (
                BotCommandScopeDefault(),
                BotCommandScopeAllPrivateChats(),
                BotCommandScopeAllGroupChats(),
                BotCommandScopeAllChatAdministrators(),
                BotCommandScopeChat(chat_id),
        ):
            await bot.delete_my_commands(scope, language_code)
            await bot.delete_my_commands(scope)


async def set_all_group_command(bot: Bot):
    return await bot.set_my_commands(
        commands=[
            BotCommand('start', 'Информация о боте'),
            BotCommand('report', 'Пожаловаться на пользователя')
        ],
        scope=BotCommandScopeAllGroupChats()
    )


async def set_chat_admins_commands(bot: Bot, chat_id: int):
    return await bot.set_my_commands(
        commands=[
            BotCommand('ro', 'Мут пользователя'),
            BotCommand('ban', 'Забанить пользователя'),
            BotCommand('reset_commands', 'Сбросить команды')
        ],
        scope=BotCommandScopeChatAdministrators(chat_id)
    )
