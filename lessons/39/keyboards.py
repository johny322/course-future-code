from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button1 = KeyboardButton('Привет!')

keyboard_hi = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=4)
# keyboard_hi.add(button1)
# keyboard_hi.add(button1, button1)
keyboard_hi.add(button1).add(button1, button1, button1, button1, button1)

button1 = KeyboardButton('1')
button2 = KeyboardButton('2')
button3 = KeyboardButton('3')

kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button1).add(button2).add(button3)

kb2 = ReplyKeyboardMarkup(resize_keyboard=True).row(button1, button2, button3, button3, button3)

kb3 = ReplyKeyboardMarkup().row(button1, button2, button3).add(KeyboardButton('Средний ряд'))

button4 = KeyboardButton('4')
button5 = KeyboardButton('5')
button6 = KeyboardButton('6')

kb3.row(button4, button5)
kb3.insert(button6)

kb4 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт', request_contact=True)
).add(
    KeyboardButton('Отправить свою локацию', request_location=True)
)

kb5 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Отправить свой контакт', request_contact=True)
        ],
        [
            KeyboardButton('Отправить свою локацию', request_location=True),
            KeyboardButton('Привет'),
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)

back_button_text = 'В главное меню'
food_button_text = 'Еда'
drink_button_text = 'Напитки!'

back_button = KeyboardButton(text=back_button_text)


class TestKeyboard(ReplyKeyboardMarkup):
    def __init__(self):
        super().__init__(resize_keyboard=True)
        self.add(KeyboardButton(text='Hi'))


class StartKeyboard(ReplyKeyboardMarkup):
    def __init__(self):
        super().__init__(resize_keyboard=True)
        self.add(KeyboardButton(text=food_button_text))
        self.add(KeyboardButton(text=drink_button_text))
        self.add(KeyboardButton(text='Ничего не хочу'))


class FoodKeyboard(ReplyKeyboardMarkup):
    def __init__(self, back=True):
        super().__init__(resize_keyboard=True)
        self.add(KeyboardButton(text='Бургер'))
        self.add(KeyboardButton(text='Пицца'))
        if back:
            self.add(back_button)


class DrinkKeyboard(ReplyKeyboardMarkup):
    def __init__(self):
        super().__init__(resize_keyboard=True)
        self.add(KeyboardButton(text='Вода'))
        self.add(KeyboardButton(text='Кола'))
        self.add(back_button)


# drink_keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text='Вода')
#         ],
#         [
#             KeyboardButton(text='Кола')
#         ],
#         [
#             back_button
#         ]
#     ],
#     resize_keyboard=True
# )

def drink_keyboard(back=True):
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    keyboard.add(KeyboardButton(text='Вода'))
    keyboard.add(KeyboardButton(text='Кола'))
    if back:
        keyboard.add(back_button)
    return keyboard
