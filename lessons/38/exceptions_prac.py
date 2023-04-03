import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Update

from config import TOKEN

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    non_existing_user = 111111
    # не попадает в error handler, так как обрабатывается try..except
    try:
        await message.answer("Неправильно закрыт <b>тег<b>")
    except Exception as err:
        await message.answer(f'Не попало в error handler. Ошибка {err}')

    # не попадает в error handler, так как обрабатывается try..except
    try:
        await bot.send_message(chat_id=non_existing_user, text='Несуществующий пользователь')
    except Exception as err:
        await message.answer(f'Не попало в error handler. Ошибка {err}')

    # попадает в error handler
    logging.info('Это не выполнится, но бот не упадет')
    await message.answer('Не сущетствует <fff>тега</fff>')

    # все что ниже не выполнится
    await message.answer('hello')


@dp.errors_handler()
async def errors_handler(update: Update, exception):
    from aiogram.utils.exceptions import (Unauthorized, InvalidQueryID, TelegramAPIError,
                                          CantDemoteChatCreator, MessageNotModified, MessageToDeleteNotFound,
                                          MessageTextIsEmpty, RetryAfter,
                                          CantParseEntities, MessageCantBeDeleted, BadRequest)

    if isinstance(exception, CantDemoteChatCreator):
        logging.info("Can't demote chat creator")
        return True

    if isinstance(exception, MessageNotModified):
        logging.info('Message is not modified')
        return True
    if isinstance(exception, MessageCantBeDeleted):
        logging.info('Message cant be deleted')
        return True

    if isinstance(exception, MessageToDeleteNotFound):
        logging.info('Message to delete not found')
        return True

    if isinstance(exception, MessageTextIsEmpty):
        logging.info('MessageTextIsEmpty')
        return True

    if isinstance(exception, Unauthorized):
        logging.info(f'Unauthorized: {exception}')
        return True

    if isinstance(exception, InvalidQueryID):
        logging.exception(f'InvalidQueryID: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, CantParseEntities):
        logging.exception(f'CantParseEntities: {exception} \nUpdate: {update}', exc_info=False)
        await update.message.answer(f'Попало в error handler. CantParseEntities: {exception.args}')
        await Update.get_current().message.answer(f'Попало в error handler. CantParseEntities: {exception.args}')
        return True

    if isinstance(exception, RetryAfter):
        logging.exception(f'RetryAfter: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, BadRequest):
        logging.exception(f'BadRequest: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, TelegramAPIError):
        logging.exception(f'TelegramAPIError: {exception} \nUpdate: {update}', exc_info=False)
        return True

    logging.exception(f'Update: {update} \n{exception}')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
