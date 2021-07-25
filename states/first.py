from aiogram.dispatcher.filters.state import StatesGroup, State


class Answer(StatesGroup):
    st = State()
    product = State()
    connection = State()
    fin = State()