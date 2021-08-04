from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.new_note_c_callback import new_note_callback

new_note_cathegory = InlineKeyboardMarkup()
new_note_cathegory.add(InlineKeyboardButton(
    text='Новая',
    callback_data=new_note_callback.new(do='N')
))

new_note_cathegory.add(InlineKeyboardButton(
    text='Старая',
    callback_data=new_note_callback.new(do='O')
))
