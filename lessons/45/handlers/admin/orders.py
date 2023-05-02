from aiogram.types import Message
from loader import dp, db
from handlers.user.menu import orders
from filters import IsAdmin


@dp.message_handler(IsAdmin(), text=orders)
async def process_orders(message: Message):
    orders = db.fetchall('SELECT * FROM orders')

    if len(orders) == 0:
        await message.answer('У вас нет заказов.')
    else:
        await order_answer(message, orders)


async def order_answer(message: Message, orders):
    res = ''

    for order in orders:
        # ('fdaf', 'john', 'moscow', '3d72af77446a55a00a3109ba9daecd9c=2')
        res += f'Заказ <b>№{order[3]}</b>\n\n'

    await message.answer(res)
