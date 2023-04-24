from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData


def get_simple_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text='1')
    btn2 = KeyboardButton(text='2')
    kb.add(btn1)
    kb.add(btn2)
    return kb


def get_simple_num_kb(num):
    kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
    ).add(KeyboardButton(f'Вы перешли с кнопки {num}')).add(KeyboardButton('Закрыть'))
    return kb


def get_inline_kb():
    inline_kb = InlineKeyboardMarkup(row_width=2)
    btns = [
        InlineKeyboardButton('1', callback_data='1'),
        InlineKeyboardButton('2', callback_data='2'),
        InlineKeyboardButton('Закрыть', callback_data='close')
    ]
    inline_kb.add(*btns)
    return inline_kb


def get_inline_num_kb(num):
    inline_kb = InlineKeyboardMarkup()
    btns = [
        InlineKeyboardButton('Вперед', callback_data=f'go_{num}'),  # go_1, go_2
        InlineKeyboardButton('Назад', callback_data='back')
    ]
    inline_kb.add(*btns)
    return inline_kb


##############################################
def start_menu():
    start_menu_k = InlineKeyboardMarkup()
    button_start = InlineKeyboardButton('Начать', callback_data='startgame')
    button_cancel = InlineKeyboardButton('Отмена', callback_data='cancel')
    start_menu_k.add(button_start, button_cancel)
    return start_menu_k


def main_game_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        KeyboardButton(text='Игра случайное число')
    )
    kb.add(
        KeyboardButton(text='Игра крестики нолики')
    )

    return kb
