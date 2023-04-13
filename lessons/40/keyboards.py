from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, \
    KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Кнопка 1')
        ],
        [
            KeyboardButton(text='Кнопка 2')
        ],
    ],
    resize_keyboard=True
)

inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1_data')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

# inline_kb_full
# inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1)
#
# inline_kb_full.add(InlineKeyboardButton('кнопка 2', callback_data='btn2'))
# inline_btn_3 = InlineKeyboardButton('кнопка 3', callback_data='btn3')
# inline_btn_4 = InlineKeyboardButton('кнопка 4', callback_data='btn4')
# inline_btn_5 = InlineKeyboardButton('кнопка 5', callback_data='btn5')
#
# inline_kb_full.add(inline_btn_3, inline_btn_4, inline_btn_5)
# inline_kb_full.row(inline_btn_3, inline_btn_4, inline_btn_5)
#
# inline_kb_full.insert(InlineKeyboardButton("inline query=''", switch_inline_query=''))
# inline_kb_full.insert(InlineKeyboardButton("inline query='qwerty'", switch_inline_query='qwerty'))
# inline_kb_full.insert(InlineKeyboardButton("Inline в этом же чате", switch_inline_query_current_chat='wasd'))
#
# inline_kb_full.add(InlineKeyboardButton('Яндекс ссылка', url='https://www.yandex.ru'))

inline_kb_full = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            inline_btn_1
        ],
        [
            InlineKeyboardButton('кнопка 2', callback_data='btn2')
        ],
        [
            InlineKeyboardButton('кнопка 3', callback_data='btn3'),
            InlineKeyboardButton('кнопка 4', callback_data='btn4')
        ],
        [
            InlineKeyboardButton('кнопка 5', callback_data='btn5')
        ],
        [
            InlineKeyboardButton('кнопка 3', callback_data='btn3'),
            InlineKeyboardButton('кнопка 4', callback_data='btn4'),
            InlineKeyboardButton('кнопка 5', callback_data='btn5')
        ],
        [
            InlineKeyboardButton("query=''", switch_inline_query=''),
            InlineKeyboardButton("query='qwerty'", switch_inline_query='qwerty')
        ],
        [
            InlineKeyboardButton("Inline в этом же чате", switch_inline_query_current_chat='wasd')
        ],
        [
            InlineKeyboardButton('Яндекс', url='https://www.yandex.ru')
        ]
    ]
)


def many_data_keyboard(*args):
    callback_data = ':'.join(args)
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='несколько параметров', callback_data=callback_data)
            ]
        ]
    )
    return keyboard
