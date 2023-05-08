import logging
import aiohttp
from typing import List

import requests

from aiogram import Bot, Dispatcher, executor, types

from config import BOT_TOKEN, TOKEN_KINO, ADMINS
from keyboards import main_menu, randon_film_kb

logging.basicConfig(level=logging.INFO)

# https://t.me/kinopoiskdev_bot
# https://kinopoisk.dev/documentation
url = 'https://api.kinopoisk.dev/'

headers = {'accept': 'application/json', 'X-API-KEY': TOKEN_KINO}

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
# session = aiohttp.ClientSession()
#
#
# async def on_startup(dp):
#     pass
#
#
# async def on_shutdown():
#     await session.close()


@dp.message_handler(commands=['start'])
async def get_menu(message: types.Message):
    if message.chat.id in ADMINS:
        await message.answer('Нажмите на кнопку для получения фильма', reply_markup=main_menu)


@dp.callback_query_handler(text='random')
async def get_random(callback: types.CallbackQuery):
    await bot.send_chat_action(callback.message.chat.id, types.ChatActions.TYPING)
    r = requests.get(url + 'v1/movie/random', headers=headers)
    if r.status_code == 200:
        print(r.text)
        title = r.json()['name']
        description = r.json()['description']
        year = r.json()['year']
        rating = r.json()['rating']['kp']
        poster = r.json()['poster']['url']

        await bot.answer_callback_query(callback.id)
        await bot.send_message(callback.from_user.id, f'Фильм: {title}')
        await bot.send_photo(callback.from_user.id, photo=poster)
        await bot.send_message(callback.from_user.id, f'Описание: {description}')
        await bot.send_message(callback.from_user.id, f'Год выхода: {year}')
        await bot.send_message(callback.from_user.id, f'Рейтинг: {rating}', reply_markup=randon_film_kb)


@dp.callback_query_handler(text='reviews')
async def get_reviews(callback: types.CallbackQuery):
    await bot.send_chat_action(callback.message.chat.id, types.ChatActions.TYPING)
    r = requests.get(url + 'v1/review?page=1&limit=10', headers=headers)
    if r.status_code == 200:
        r = r.json()['docs']
        await bot.answer_callback_query(callback.id)
        for rw in r[5:8]:
            id = rw['movieId']
            r_film = requests.get(url + 'v1.3/movie/' + str(id), headers=headers)
            # print(r_film.json())
            title_film = r_film.json()['name']
            title = rw['title']
            review = rw['review']
            print(review)
            author = rw['author']
            if title_film:
                await bot.send_message(callback.from_user.id, f'Фильм: {title_film}')
            await bot.send_message(callback.from_user.id, f'Заголовок: {title}')
            await bot.send_message(callback.from_user.id, f'Обзор: {review}')
            await bot.send_message(callback.from_user.id, f'Автор: {author}')
            await bot.send_message(callback.from_user.id, '________________')
        await callback.message.answer('Отзывы закончились')


@dp.message_handler(commands='search', chat_id=ADMINS)
async def search_handler(message: types.Message):
    await bot.send_chat_action(message.chat.id, types.ChatActions.TYPING)
    film_name = message.get_args()
    print(f"{film_name=}")
    if not film_name:
        await message.answer('отправьте команду с названием фильма\n'
                             'Пример: /search человек паук')
        return
    # https://docs.aiohttp.org/en/stable/client_quickstart.html#make-a-request
    # async with aiohttp.ClientSession() as session:
    #     r = await session.get(url + f'v1.3/movie?name={film_name}', headers=headers)
    # if r.status == 200:
    #     data = await r.json()
    #     docs: List[dict] = data['docs']
    #     for doc in docs:
    #         name = doc['name']
    #         year = doc['year']
    #         rating = doc['rating']['kp']
    #         poster = doc['poster']['url']
    #         text = f'Фильм: {name}\n' \
    #                f'Год выхода: {year}\n' \
    #                f'Рейтинг: {rating}'
    #         await message.answer_photo(
    #             photo=poster,
    #             caption=text
    #         )
    async with aiohttp.ClientSession() as session:
        async with session.get(url + f'v1.3/movie?name={film_name}', headers=headers) as resp:
            print(resp)
            if resp.status == 200:
                data = await resp.json()
                docs: List[dict] = data['docs']
                for doc in docs:
                    name = doc['name']
                    year = doc['year']
                    rating = doc['rating']['kp']
                    poster = doc['poster']['url']
                    text = f'Фильм: {name}\n' \
                           f'Год выхода: {year}\n' \
                           f'Рейтинг: {rating}'
                    await message.answer_photo(
                        photo=poster,
                        caption=text
                    )
    # r = requests.get(url + f'v1.3/movie?name={film_name}', headers=headers)
    # if r.status_code == 200:
    #     print(r.text)
    #     docs: List[dict] = r.json()['docs']
    #     for doc in docs:
    #         name = doc['name']
    #         year = doc['year']
    #         rating = doc['rating']['kp']
    #         poster = doc['poster']['url']
    #         text = f'Фильм: {name}\n' \
    #                f'Год выхода: {year}\n' \
    #                f'Рейтинг: {rating}'
    #         await message.answer_photo(
    #             photo=poster,
    #             caption=text
    #         )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
