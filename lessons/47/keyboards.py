from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_menu = InlineKeyboardMarkup()
btn_search = InlineKeyboardButton('Случайный фильм', callback_data='random')
btn_reviews = InlineKeyboardButton('Отзывы', callback_data='reviews')
main_menu.add(btn_search, btn_reviews)

randon_film_kb = InlineKeyboardMarkup()
btn_new_film = InlineKeyboardButton('Другой фильм', callback_data='random')
randon_film_kb.add(btn_new_film)
