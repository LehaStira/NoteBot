from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart


from keyboards.inline.start_menu import start_choice
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
    await message.answer(f'Что сегодня будем делать?', reply_markup=start_choice)
