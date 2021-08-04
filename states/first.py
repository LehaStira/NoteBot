from aiogram.dispatcher.filters.state import StatesGroup, State


class Answer(StatesGroup):
    adding_new_cathegory = State()
    old_cathegory = State()
    new_note_new_cathegory = State()
    connection = State()
    fin = State()