import datetime
import logging

import requests
from aiogram import Bot, Dispatcher, types, executor

from config import TOKEN, WEATHER_API

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


def get_weather(city_name) -> str:
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Ясно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHER_API}&units=metric')
    data = r.json()
    print(data)
    city = data['name']
    cur_weather = data['main']['temp']

    weather_description = data['weather'][0]['main']
    if weather_description in code_to_smile:
        wd = code_to_smile[weather_description]
    else:
        wd = 'Посмотри в окно сам'
    humidity = data['main']["humidity"]
    pressure = data['main']['pressure']
    sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
    sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
    length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - \
                        datetime.datetime.fromtimestamp(data['sys']['sunrise'])
    wind = data['wind']['speed']
    text = f'***{datetime.datetime.now().strftime("%d.%m.%Y %H:%M")}***\n' \
           f'Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n' \
           f'Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/c\n' \
           f'Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n' \
           f'Хорошего дня!'
    return text


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await message.answer('Привет я бот погоды\nЧтобы узнать погоду просто введи название города!')


@dp.message_handler()
async def get_weather_handler(message: types.Message):
    try:
        text = get_weather(message.text)
        await message.answer(text)
    except Exception as err:
        await message.reply('Проверьте название города!')
        print(err)


if __name__ == '__main__':
    executor.start_polling(dp)
