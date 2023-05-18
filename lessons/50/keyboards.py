from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup()
btn_payment = InlineKeyboardButton('Оплатить', callback_data='payment')
btn_cancel = InlineKeyboardButton('Отмена', callback_data='cancel')
keyboard.add(btn_payment, btn_cancel)

keyboard_check = InlineKeyboardMarkup()
btn_check = InlineKeyboardButton('Проверить подписку', callback_data='check')
keyboard_check.add(btn_check)

disable_edv_keyboard = InlineKeyboardMarkup()
btn_payment = InlineKeyboardButton('Оплатить', callback_data='disable_edv')
btn_cancel = InlineKeyboardButton('Отмена', callback_data='cancel')
disable_edv_keyboard.add(btn_payment, btn_cancel)
