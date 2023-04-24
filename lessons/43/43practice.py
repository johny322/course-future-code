from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from config import TOKEN
from states import OrderFood

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

available_food_names = ["суши", "спагетти", "хачапури"]
available_food_sizes = ["маленькую", "среднюю", "большую"]


@dp.message_handler(commands='start', state='*')
async def start_handler(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        "Выберите, что хотите заказать: напитки (/drinks) или блюда (/food).",
        reply_markup=types.ReplyKeyboardRemove()
    )


@dp.message_handler(commands='cancel', state='*')
@dp.message_handler(Text(equals="отмена", ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands='food')
async def food_start_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    print(state, current_state)
    data = await state.get_data()
    print(f"{data=}")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in available_food_names:
        keyboard.add(name)
    await message.answer("Выберите блюдо:", reply_markup=keyboard)
    await OrderFood.waiting_for_food_name.set()
    # await state.set_state('OrderFood:waiting_for_food_name')
    # await state.set_state('food')


@dp.message_handler(state=OrderFood.waiting_for_food_name)
async def food_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    print(state, current_state)
    if message.text.lower() not in available_food_names:
        await message.answer("Пожалуйста, выберите блюдо, используя клавиатуру ниже.")
        return
    await state.update_data(chosen_food=message.text.lower())

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for size in available_food_sizes:
        keyboard.add(size)
    # await OrderFood.waiting_for_food_size.set()
    # Для последовательных шагов можно не указывать название состояния, обходясь next()
    # await OrderFood.next()
    await state.set_state(OrderFood.waiting_for_food_size)
    await message.answer("Теперь выберите размер порции:", reply_markup=keyboard)


@dp.message_handler(state=OrderFood.waiting_for_food_size)
async def food_size_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    print(state, current_state)
    if message.text.lower() not in available_food_sizes:
        await message.answer("Пожалуйста, выберите размер порции, используя клавиатуру ниже.")
        return
    user_data: dict = await state.get_data()
    print(user_data)
    food = user_data['chosen_food']
    size = message.text.lower()
    await message.answer(f"Вы заказали {size} порцию {food}.\n"
                         f"Попробуйте теперь заказать напитки: /drinks", reply_markup=types.ReplyKeyboardRemove())
    # await state.finish()
    await state.reset_state(with_data=False)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
