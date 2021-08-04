from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.new_note_c_callback import new_note_callback
from keyboards.inline.sad import sad
from keyboards.inline.sad_callback import saaaaaaaaaaad
from keyboards.inline.start_callback import start_callback
from loader import dp
from states.first import Answer


@dp.callback_query_handler(new_note_callback.filter(do='O'))
async def new_note(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer('Введи категорию: ')
    await Answer.old_cathegory.set()


@dp.message_handler(state=Answer.old_cathegory)
async def new_note(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f'Тут, дорогой {message.from_user.full_name}, ты типа пишешь заметку, я сохраняю в базу')
    await message.answer(f'Но так как мне лень разворачивать базу, этого нет')
    await message.answer(f'И улитки тоже нет', reply_markup=sad)


@dp.callback_query_handler(saaaaaaaaaaad.filter(answer='Saaaad'))
async def new_note(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer('Грустно, вот так продается искусство')
    await call.message.answer('К искусству в рифму слово "капуста" ')
    await call.message.answer('К капусте вообще нет рифмы')
    await call.message.answer('Тупые гитарные рифы')


@dp.callback_query_handler(saaaaaaaaaaad.filter(answer='Good'))
async def new_note(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer('I never ask for this!')


@dp.callback_query_handler(saaaaaaaaaaad.filter(answer='Angry'))
async def new_note(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    print(f'{call.from_user.full_name} Попался!.')
    for i in range(0, 50000):
        await call.message.answer('Я знаю циклы, а ты идешь нах')
