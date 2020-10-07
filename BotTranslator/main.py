# t.me/mow_tr_bot  - link to the bot
from BotTranslator import config  # imports from config.py
import telebot  # pyTelegramBotAPI
from telebot import types
from googletrans import Translator  # free and unlimited python library that implemented Google Translate API


bot = telebot.TeleBot(config.token)  # creates a new Telegram Bot object
translator = Translator()  # creates a new Translator object


@bot.message_handler(commands=['start'])  # /start command
def send_welcome(message):
    bot.reply_to(message, '''
    Привет! Я помогу тебе с переводом. \nПока я перевожу только с английского на русский\
    /change_language - комманда, чтобы выбрать\\сменить язык\
    Успехов!''')


keyboard = types.InlineKeyboardMarkup()
keyboard.add(types.InlineKeyboardButton('Русский', callback_data='ru'),
             types.InlineKeyboardButton('Английский', callback_data='en'),
             types.InlineKeyboardButton('Немецкий', callback_data='de'),
             types.InlineKeyboardButton('Украинский', callback_data='uk'))


@bot.message_handler(commands=['change_language'])  # /change_language command
def src_language(message):
    cid = message.chat.id
    bot.send_message(cid, 'С какого языка вы хотите перевести?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def dest_language(call):
    if call.data in ['ru', 'en', 'de', 'uk']:
        bot.send_message(call.message.chat.id, text='На какой язык вы хотите перевести?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call:True)
def call_answer(call):
    if call.data in ['ru', 'en', 'de', 'uk']:
        bot.send_message(call.message.chat.id, text="Теперь введите ваше сообщение")


@bot.message_handler(content_types=['text'])  # translates text of the message to russian
def bot_trans(message):
    result = translator.translate(message.text, dest='ru')
    trans_text = result.text
    bot.send_message(message.chat.id, trans_text)


if __name__ == '__main__':
    bot.polling(none_stop=True)  # tells the bot to try not to stop if any errors occur
