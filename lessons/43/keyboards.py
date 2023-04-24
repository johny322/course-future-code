from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData


def towns():
    list_button_name = [['Москва', 'Санкт Петербург', 'Нижний Новгород', 'Ростов'],
                        ['Новосибирск', 'Екатеринбург', 'Казань', 'Челябинск']]

    buttons_list = []
    for item in list_button_name:
        l = []
        for i in item:
            l.append(InlineKeyboardButton(text=i, callback_data=i))
        buttons_list.append(l)

    keyboard_inline = InlineKeyboardMarkup(inline_keyboard=buttons_list)
    return keyboard_inline
