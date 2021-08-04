from aiogram.types import CallbackQuery

from keyboards.inline.new_note_c_callback import new_note_callback
from keyboards.inline.start_callback import start_callback
from loader import dp
from states.first import Answer


@dp.callback_query_handler(new_note_callback.filter(do='N'))
async def new_note(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer('Введи категорию: ')
    await Answer.adding_new_cathegory.set()