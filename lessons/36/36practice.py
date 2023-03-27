import logging

from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import filters, FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN, ADMIN_ID
from middlewares import SomeMiddleware

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)


# forbidden_words = ['bad', 'word']
#
#
# @dp.message_handler(hashtags=['hi', 'photo'])
# async def hashtag_handler(message: types.Message):
#     await message.answer('тут есть хештег hi или photo')
#
#
# # @dp.message_handler(cashtags='hi')
# # async def hashtag_handler(message: types.Message):
# #     await message.answer('тут есть кештег hi')
#
# # @dp.message_handler(filters.Regexp('^\d{2,}'))
# # async def regexp_handler(message: types.Message):
# #     await message.answer('сообщение начинается с цифры')
#
#
# @dp.message_handler(regexp=r'^\d{2,}', is_forwarded=False)
# async def regexp_handler(message: types.Message):
#     await message.answer('сообщение начинается с цифры')
#
#
# # @dp.message_handler(filters.RegexpCommandsFilter([r'/digits:\d{3}', r'/digits.\d{3}']))
# # async def regexp_command_handler(message: types.Message):
# #     await message.answer('команда с 3 цифрами')
#
#
# @dp.message_handler(regexp_commands=[r'/digits:\d{3}', r'/digits.\d{3}'])
# async def regexp_command_handler(message: types.Message):
#     await message.answer('команда с 3 цифрами')
#
#
# @dp.message_handler(commands=['state'])
# async def set_state_handler(message: types.Message, state: FSMContext):
#     await state.set_state('state1')
#     await message.answer('тебе установлено состояние state1')
#
#
# @dp.message_handler(state='state1')
# async def state_handler(message: types.Message, state: FSMContext):
#     print(state)
#     current_state = await state.get_state()
#     print(current_state)
#
#     await state.finish()
#
#
# @dp.message_handler(filters.Text(startswith=forbidden_words, ignore_case=True))
# async def text_filter_handler(message: types.Message):
#     await message.answer('Это запрещенные слова')
#
#
# # @dp.message_handler(filters.IDFilter(user_id=ADMIN_ID), commands='admin')
# # async def id_filter_handler(message: types.Message):
# #     await message.answer('привет админ')
#
#
# @dp.message_handler(chat_id=ADMIN_ID, commands='admin')
# async def id_filter_handler(message: types.Message):
#     await message.answer('привет админ')
#
#
# @dp.message_handler(filters.AdminFilter(), commands='photo')
# async def is_admin_filter_handler(message: types.Message):
#     await bot.send_message(message.from_user.id, 'вы админ чата')
#     await message.answer('вы админ чата')
#
#
# @dp.message_handler(is_reply=True, commands='user_id')
# async def reply_filter_handler(message: types.Message):
#     await message.answer(message.reply_to_message.from_user.id)
#
#
# # @dp.message_handler(is_forwarded=True)
# # async def forwarded_filter_handler(message: types.Message):
# #     await message.answer('Ты переслал мне сообщение')
#
#
# @dp.message_handler(is_forwarded=True, chat_type='group')
# async def forwarded_filter_handler(message: types.Message):
#     await message.answer('Ты переслал мне сообщение')


@dp.message_handler()
async def echo_handler(message: types.Message, middleware_data1, middleware_data2, user_id, user: dict, is_blocked: bool):
    print('echo_handler')
    print(f'{user=}, {middleware_data1=}, {middleware_data2=}')
    print(message.text)
    is_blocked_text = 'вы в бане' if is_blocked else 'вы не в бане'
    # if is_blocked:
    #     is_blocked_text = 'вы в бане'
    # else:
    #     is_blocked_text = 'вы не в бане'

    await message.answer(f'Твой id: <b>{user_id}</b>\n'
                         f'Твой баланс: <i>{user.get("balance")}</i>\n'
                         f'{is_blocked_text}\n'
                         f'Текст: {message.text}',
                         parse_mode='HTML')
    return {'handler_data': 'some handler data'}


# on_<point>_<event_type>
# on_pre_process_message, on_post_process_update

async def on_startup(dp: Dispatcher):
    dp.middleware.setup(SomeMiddleware())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
