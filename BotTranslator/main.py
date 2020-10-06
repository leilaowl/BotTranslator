# t.me/mow_tr_bot  - link to the bot
from BotTranslator import config  # imports from config.py
import telebot  # pyTelegramBotAPI
from googletrans import Translator  # free and unlimited python library that implemented Google Translate API


bot = telebot.TeleBot(config.token)  # creates a new Telegram Bot object
translator = Translator()  # creates a new Translator object


@bot.message_handler(commands=['start'])  # /start command
def send_welcome(message):
    bot.reply_to(message, 'Привет! Я помогу тебе с переводом. \nПока я перевожу только с английского на русский :)')


@bot.message_handler(content_types=['text'])  # translates text of the message to russian
def translate(message):
    result = translator.translate(message.text, dest='ru')
    trans_text = result.text
    bot.send_message(message.chat.id, trans_text)


if __name__ == '__main__':
    bot.polling(none_stop=True)  # tells the bot to try not to stop if any errors occur
