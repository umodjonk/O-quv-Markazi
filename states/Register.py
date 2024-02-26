from aiogram.dispatcher.filters.state import State, StatesGroup


class RegisterState(StatesGroup):
    name = State()
    age = State()
    course = State()
    rank = State()
    number = State()
    rate = State()
    check = State()