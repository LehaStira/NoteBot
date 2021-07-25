from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from keyboards.inline.new_note_c import new_note_cathegory
from keyboards.inline.start_callback import start_callback
from keyboards.inline.start_menu import start_choice
from loader import dp


@dp.callback_query_handler(start_callback.filter(doing='New'))
async def new_note(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer('Категория... ', reply_markup=new_note_cathegory)