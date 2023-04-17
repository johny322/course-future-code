from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

random_keyboard = InlineKeyboardMarkup()
random_keyboard.add(InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))


def get_keyboard():
    buttons = [
        InlineKeyboardButton(text="-1", callback_data="num_decr"),
        InlineKeyboardButton(text="+1", callback_data="num_incr"),
        InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


callback_numbers = CallbackData("fabnum", "action")


def get_keyboard_fab():
    buttons = [
        InlineKeyboardButton(text="-1", callback_data=callback_numbers.new(action="decr")),
        InlineKeyboardButton(text="+1", callback_data=callback_numbers.new(action="incr")),
        InlineKeyboardButton(text="Подтвердить", callback_data=callback_numbers.new(action="finish", arg='123'))
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def main_menu():
    menu_kb = InlineKeyboardMarkup(row_width=2)
    pizza_button = InlineKeyboardButton(text='Пицца 🍕', callback_data='pizza_cat')
    snacks_button = InlineKeyboardButton(text='Закуски 🍟', callback_data='snacks_cat')
    menu_kb.insert(pizza_button)
    menu_kb.insert(snacks_button)
    return menu_kb


pizza_callback = CallbackData("pizza_menu", "name", "id")
back_callback = CallbackData("back", "menu")


def menu_pizza_kb(names: list):
    menu_kb = InlineKeyboardMarkup(row_width=2)
    for pizza_id, name in enumerate(names, start=1):
        pizza_button = InlineKeyboardButton(
            text=f'Пицца {name}',
            callback_data=pizza_callback.new(name=name, id=pizza_id)
        )
        menu_kb.insert(pizza_button)

    menu_kb.row(InlineKeyboardButton(text='Назад', callback_data=back_callback.new(menu='start')))
    return menu_kb


if __name__ == '__main__':
    print(callback_numbers.new(action="decr"))
