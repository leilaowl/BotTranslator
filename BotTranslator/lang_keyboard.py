# creating a keyboard for selecting languages
from BotTranslator import config
from telebot import types


keyboard = types.InlineKeyboardMarkup()
for i, j in config.LANGDICT.items():
    key = types.InlineKeyboardButton(j, callback_data=i)
    keyboard.add(key)


"""
keyboard = types.InlineKeyboardMarkup()
keyboard.add(types.InlineKeyboardButton('Русский', callback_data='ru'),
             types.InlineKeyboardButton('Английский', callback_data='en'),
             types.InlineKeyboardButton('Немецкий', callback_data='de'),
             types.InlineKeyboardButton('Украинский', callback_data='uk'))

"""
