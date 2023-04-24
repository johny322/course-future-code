import json

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from config import TOKEN
from keyboards import towns
from states import CallbackOnStart

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(Command('onstarttest'))
async def start_test_handler(message: types.Message):
    id = message.from_user.id
    with open('users_test_one.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    user = True
    for i in data:
        if int(i) == id:
            user = False
            break

    if user:
        await message.answer("Описание опросника")
        await message.answer('Вопрос №1\nСколько вам лет?\nНапишите ответ (только число)',
                             reply_markup=ReplyKeyboardRemove())
        await CallbackOnStart.Q1.set()
    else:
        await message.answer(text="Вы уже проходили тест")


@dp.message_handler(state=CallbackOnStart.Q1)
async def towns_handler(message: types.Message, state: FSMContext):
    reply_markup = towns()
    answer = message.text
    await state.update_data(age=answer)
    await message.answer(text="Вопрос №2\nВ каком городе вы живете?\nВыберите ответ из предложенных",
                         reply_markup=reply_markup)
    await state.set_state(CallbackOnStart.Q2)
    # await CallbackOnStart.next()


@dp.callback_query_handler(state=CallbackOnStart.Q2)
async def end_handler(call: types.CallbackQuery, state: FSMContext):
    answer = call.data
    await state.update_data(full_name=call.from_user.full_name, town=answer)
    data = await state.get_data()
    user = {call.from_user.id: data}
    text = []
    for i in data:
        text.append(f'{data[i]}\n')
    await call.message.answer(text="Ваши ответы:", reply_markup=ReplyKeyboardRemove())
    await call.message.answer('\n'.join(text))
    await call.answer()
    with open('users_test_one.json', encoding='utf-8') as file:
        data = json.load(file)
        data.update(user)
    with open('users_test_one.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
