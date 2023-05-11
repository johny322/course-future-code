import logging
from dataclasses import dataclass
from typing import List

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command

from config import BOT_TOKEN, PROVIDER_TOKEN

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.DEBUG)


@dataclass
class Item:
    title: str
    description: str
    start_parameter: str
    currency: str
    prices: List[types.LabeledPrice]
    provider_data: dict = None
    photo_url: str = None
    photo_size: int = None
    photo_width: int = None
    photo_height: int = None
    need_name: bool = False
    need_phone_number: bool = False
    need_email: bool = False
    need_shipping_address: bool = False
    send_phone_number_to_provider: bool = False
    send_email_to_provider: bool = False
    is_flexible: bool = False
    provider_token: str = PROVIDER_TOKEN

    def generate_invoices(self):
        return self.__dict__


NoteBook = Item(
    title='Ноутбук Lenovo IP Gaming 3',
    description='Выведите игровой процесс киберспортивных дисциплин на новый уровень с помощью устройства, которое поможет опередить конкурентов и занять первые строчки в списках лидеров',
    currency='RUB',
    prices=[
        types.LabeledPrice(
            label='Ноутбук Lenovo IP Gaming 3',
            amount=30_000_25
        ),
        types.LabeledPrice(
            label='Доставка',
            amount=500_00
        ),
        types.LabeledPrice(
            label='Скидка',
            amount=-2_000_00
        )

    ],
    need_name=True,
    start_parameter='create_invoice_lenovo_3',
    photo_url="https://items.s1.citilink.ru/1595005_v01_b.jpg",
    photo_size=600,
    need_shipping_address=True,
    is_flexible=True
)

POST_REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title='Почтой',
    prices=[
        types.LabeledPrice(
            'Обычная коробка', 0
        ),
        types.LabeledPrice(
            'Почтой', 500_00
        ),
    ]
)

POST_FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Почтой ускоренная',
    prices=[
        types.LabeledPrice(
            'Прочная упаковка', 200_00
        ),
        types.LabeledPrice(
            'Срочной почтой', 1000_00
        ),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(
    id='pickup',
    title='Самовывоз',
    prices=[
        types.LabeledPrice(
            'Самовывоз из магазина', -100_00
        ),
    ]
)


@dp.message_handler(Command('invoices'))
async def show_invoices(message: types.Message):
    await bot.send_invoice(message.from_user.id, **NoteBook.generate_invoices(), payload='12345')


# @dp.shipping_query_handler(lambda query: query.invoice_payload == '12345')
@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    print(query.invoice_payload)
    if query.shipping_address.country_code == 'RU':
        await bot.answer_shipping_query(shipping_query_id=query.id, shipping_options=[
            POST_REGULAR_SHIPPING,
            POST_FAST_SHIPPING,
            PICKUP_SHIPPING
        ],
                                        ok=True)
    elif query.shipping_address.country_code == 'US':
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False, error_message='Сюда не доставляем')
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[POST_REGULAR_SHIPPING],
                                        ok=True)


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(query: types.PreCheckoutQuery):
    print(f"{query.invoice_payload=}")
    print(f"{query.order_info.shipping_address=}")
    print(f"{query.shipping_option_id=}")
    if query.shipping_option_id == 'post_fast':
        ok = False
        error_message = 'Сейчас нет такой доставки'
    else:
        ok = True
        error_message = None
    await bot.answer_pre_checkout_query(pre_checkout_query_id=query.id, ok=ok, error_message=error_message)
    if ok:
        await bot.send_message(chat_id=query.from_user.id, text='Спасибо за покупку')
    else:
        await bot.send_message(chat_id=query.from_user.id, text='Ошибка')


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
    # print(NoteBook)
    # print(NoteBook.generate_invoices())
