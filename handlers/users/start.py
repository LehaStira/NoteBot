from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from keyboards.inline.start_callback import start_callback
from keyboards.inline.start_menu import start_choice
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
    await message.answer(f'Что сегодня будем делать?', reply_markup=start_choice)


@dp.callback_query_handler(start_callback.filter(doing='Old'))
async def new_note(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer('Тута нужна база, тута ничего нет, жми старт')