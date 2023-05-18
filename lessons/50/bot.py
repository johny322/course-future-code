import logging
from typing import Optional

from aiogram import executor, types, Bot, Dispatcher
from aiogram.types import ContentType
from config import BOT_TOKEN, Y_TOKEN, ADMINS
from keyboards import keyboard_check, keyboard, disable_edv_keyboard

logging.basicConfig(level=logging.DEBUG)


def get_subscribers() -> list:
    # обращение к бд
    return []


def update_user(user_id, subscribe: Optional[bool], disable: Optional[bool]):
    if subscribe is not None:
        # обращение к бд
        # изменение значения столбца subscribe на subscribe
        print('обновляем статус подписки')
    if disable is not None:
        # обращение к бд
        # изменение значения столбца disable на disable
        print('обновляем статус рассылки')


subscribers = []
disables = []

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    id = message.from_user.id

    if id in subscribers or id in ADMINS:
        username = message.from_user.username
        await message.answer(f'Добро пожаловать {username}')
    else:
        await message.answer('Для начала работы вам необходимо подписаться', reply_markup=keyboard)


@dp.message_handler(commands=['disable'])
async def disable_handler(message: types.Message):
    id = message.from_user.id
    if id not in disables:
        await message.answer('Для отключения рекламы оплатите', reply_markup=disable_edv_keyboard)
    else:
        await message.answer('Вы не получаете рекламную рассылку')


@dp.message_handler(commands=['help'])
async def help_message(message: types.Message):
    await message.answer('Вы находитесь в информационном боте\n'
                         'Для взаимодействия с ботом необходима подписка\n'
                         'Если вы оформили подписку и она не активна напишите'
                         'пожалуйста администраторам @abrareq', reply_markup=keyboard_check)


@dp.callback_query_handler(text='payment')
async def payment(callback: types.CallbackQuery):
    await bot.send_invoice(
        chat_id=callback.from_user.id, title='Подписка', description='Подписка на бота',
        payload='payment', provider_token=Y_TOKEN, currency='RUB', start_parameter='test_bot',
        prices=[types.LabeledPrice('Подписка', 10000)],
        # prices=[{'label': 'Подписка', 'amount': 10000}],

    )
    await callback.answer()


@dp.callback_query_handler(text='disable_edv')
async def disable_edv_handler(callback: types.CallbackQuery):
    await bot.send_invoice(
        chat_id=callback.from_user.id, title='Отключение рекламы', description='Отключение рекламы',
        payload='disable_edv', provider_token=Y_TOKEN, currency='RUB', start_parameter='test_bot',
        prices=[types.LabeledPrice('Отключение рекламы', 500_13)],

    )
    await callback.answer()


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(lambda message: message.successful_payment.invoice_payload == 'disable_edv',
                    content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: types.Message):
    await message.answer('Вы успешно отключили рекламу')
    disables.append(message.from_user.id)
    update_user(
        message.from_user.id,
        subscribe=None,
        disable=True
    )


@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: types.Message):
    if message.successful_payment.invoice_payload == 'payment':
        await bot.send_message(message.from_user.id, 'Вы подписались')
        subscribers.append(message.from_user.id)
        update_user(
            message.from_user.id,
            subscribe=True,
            disable=None
        )
    # elif message.successful_payment.invoice_payload == 'disable_edv':
    #     await message.answer('Вы успешно отключили рекламу')
    #     disables.append(message.from_user.id)


@dp.callback_query_handler(text='check')
async def check_sub(callback: types.CallbackQuery):
    id = callback.from_user.id
    if id in ADMINS:
        await callback.message.edit_text('Вы являетесь администратором')
    elif id in subscribers:
        await callback.message.edit_text('Подписка активирована')
    else:
        await callback.message.edit_text('Подписка не активна', reply_markup=keyboard)
    await callback.answer()


@dp.callback_query_handler(text='cancel')
async def push_cancel(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Вы отказались от подписки\nДля дальнейшей работы с ботом необходима подписка')
    # await callback.message.answer('Вы отказались от подписки\nДля дальнейшей работы с ботом необходима подписка')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
