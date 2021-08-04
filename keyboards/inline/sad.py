from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.sad_callback import saaaaaaaaaaad

sad = InlineKeyboardMarkup()
sad.add(InlineKeyboardButton(
    text='Грустно(',
    callback_data=saaaaaaaaaaad.new(answer='Saaaad')
))

sad.add(InlineKeyboardButton(
    text='Спасибо, Ляксей и на том!',
    callback_data=saaaaaaaaaaad.new(answer='Good')
))

sad.add(InlineKeyboardButton(
    text='Пшел нах!',
    callback_data=saaaaaaaaaaad.new(answer='Angry')
))