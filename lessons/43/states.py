from aiogram.dispatcher.filters.state import StatesGroup, State


class OrderFood(StatesGroup):
    waiting_for_food_name = State()
    waiting_for_food_size = State()


class CallbackOnStart(StatesGroup):
    Q1 = State()
    Q2 = State()
