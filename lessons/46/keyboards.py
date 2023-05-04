from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

check_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Проверить подписки', callback_data="check_subs")
        ]
    ]
)

post_callback = CallbackData("create_post", "action")
confirmation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Опубликовать пост", callback_data=post_callback.new(action="post")),
            InlineKeyboardButton(text="Отклонить", callback_data=post_callback.new(action="cancel"))
        ]
    ]
)
