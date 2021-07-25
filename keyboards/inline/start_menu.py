from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.start_callback import start_callback

start_choice = InlineKeyboardMarkup()
start_choice.add(InlineKeyboardButton(
    text='Новая заметка',
    callback_data=start_callback.new(doing='New')
))

start_choice.add(InlineKeyboardButton(
    text='Посмотреть старые заметки',
    callback_data=start_callback.new(doing='Old')
))
