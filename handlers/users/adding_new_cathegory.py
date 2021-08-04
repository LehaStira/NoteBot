from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import GLOBAL_DIC
from loader import dp
from states.first import Answer


@dp.message_handler(state=Answer.adding_new_cathegory)
async def new_note(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f'Ваша категория {message.text}')
    GLOBAL_DIC.setdefault(message.text)
    await message.answer(f'Потом я крч зафигачу это в базу, но сейчас базу лень разворачивать, поэтому держи улитку')
    __logo__ = r"""
                         _   _             
                         @   @
               / .-"-.`.  \ /
              | | '\ \ \_/ )
           ,-\ `-.' /.'  /
           '---`----'----'
               """
    await message.answer(__logo__)
    await message.answer('Введите вашу заметку: ')
    await Answer.new_note_new_cathegory.set()


@dp.message_handler(state=Answer.new_note_new_cathegory)
async def new_note(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f'Ваша заметка: {message.text}')
    await message.answer(f'Потом я крч зафигачу это в базу, но сейчас базу лень разворачивать, поэтому держи улитку')
    __logo__ = r"""
                         _   _             
                         @   @
               / .-"-.`.  \ /
              | | '\ \ \_/ )
           ,-\ `-.' /.'  /
           '---`----'----'
               """
    await message.answer(__logo__)
    await message.answer('Нажми снова старт')