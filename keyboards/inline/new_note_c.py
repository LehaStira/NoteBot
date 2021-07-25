from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.start_callback import start_callback

new_note_cathegory = InlineKeyboardMarkup()
new_note_cathegory.add(InlineKeyboardButton(
    text='Новая',
    callback_data=start_callback.new(doing='New')
))

new_note_cathegory.add(InlineKeyboardButton(
    text='Старая',
    callback_data=start_callback.new(doing='Old')
))
