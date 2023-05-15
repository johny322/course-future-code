import datetime
import logging
import os
import uuid
from dataclasses import dataclass

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hlink, hcode

from config import BOT_TOKEN
from items import items
from keyboards import buy_keyboard, paid_keyboard

storage = MemoryStorage()
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)


# pip install qiwipy
# https://developer.qiwi.com/ru/qiwi-wallet-personal/#intro
# import pyqiwi
# wallet = pyqiwi.Wallet(token=os.getenv('QIWI_TOKEN'), number=os.getenv('WALLET_QIWI'))
@dataclass
class Total:
    amount: float


@dataclass
class Transaction:
    comment: str
    total: Total


class Wallet:
    def __init__(self, token, number):
        self.token = token
        self.number = number

    def history(self, *args, **kwargs):
        history = {
            'transactions': [
                Transaction('1243', Total(123.4)),
                Transaction('22222', Total(2.4)),
                Transaction('fdasfa', Total(1000)),
                Transaction('f766c350-40d5-4884-a165-ecfc8de21082', Total(100)),

            ]
        }
        return history


class NotEnougnMoney(Exception):
    pass


class NotPaymentFound(Exception):
    pass


wallet = Wallet(token=os.getenv('QIWI_TOKEN'), number=os.getenv('WALLET_QIWI'))


@dataclass
class Payment:
    amount: int
    id: str = None

    def create(self):
        self.id = str(uuid.uuid4())
        # print(self.id)
        # self.id = 'f766c350-40d5-4884-a165-ecfc8de21082'

    def check_payment(self):
        start_date = datetime.datetime.now() - datetime.timedelta(days=2)
        transactions = wallet.history(start_date=start_date).get('transactions')
        for transaction in transactions:
            if transaction.comment:
                if str(self.id) in transaction.comment:
                    if float(transaction.total.amount) >= float(self.amount):
                        return True
                    else:
                        raise NotEnougnMoney
        else:
            raise NotPaymentFound

    @property
    def invoice(self):
        link = 'https://oplata.qiwi.com/create?publicKey={publicKey}&amount={amount}&comment={comment}'
        return link.format(publicKey=os.getenv('QIWI_PUB'), amount=self.amount, comment=self.id)


@dp.message_handler(Command('items'))
async def show_items(message: types.Message):
    caption = """
    Название продукта: {title}
    <i>Описание:</i>
    {description}

    <u>Цена:</u> {price:.2f} <b>RUB</b>
    """
    for item in items:
        await message.answer_photo(
            photo=item.photo_link,
            caption=caption.format(
                title=item.title,
                description=item.description,
                price=item.price
            ),
            reply_markup=buy_keyboard(item_id=item.id)
        )


@dp.callback_query_handler(text_contains='buy')
async def create_invoice(call: types.CallbackQuery, state: FSMContext):
    item_id = call.data.split(':')[-1]
    item_id = int(item_id) - 1
    item = items[item_id]
    amount = item.price

    payment = Payment(amount=amount)
    payment.create()

    await call.message.answer(
        "\n".join(
            [
                f'Оплатите не менее {amount:.2f} по номеру телефона или по адресу',
                "",
                hlink(os.getenv('WALLET_QIWI'), url=payment.invoice),
                "И обязательно укажите ID платежа:",
                hcode(payment.id)
            ]
        ),
        reply_markup=paid_keyboard
    )
    await state.set_state("qiwi")
    await state.update_data(payment=payment)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='paid', state='qiwi')
async def approve_payment(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    payment: Payment = data.get('payment')
    try:
        payment.check_payment()
    except NotPaymentFound:
        await call.message.answer('Транзакция не найдена')
        return
    except NotEnougnMoney:
        await call.message.answer('Недостаточная сумма')
        return
    else:
        await call.message.answer('Успешная оплата')
        await call.message.delete_reply_markup()
        await state.finish()


@dp.callback_query_handler(text='cancel', state='qiwi')
async def cancel_payment(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text('Отменено')
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
