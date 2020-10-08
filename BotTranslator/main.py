# t.me/mow_tr_bot  - link to the bot
from BotTranslator import config  # imports from config.py
from BotTranslator import lang_keyboard  # imports from keyboard.py
import telebot  # pyTelegramBotAPI
# from telebot import types
from googletrans import Translator  # free and unlimited python library that implemented Google Translate API


bot = telebot.TeleBot(config.TOKEN)  # creates a new Telegram Bot object
translator = Translator()  # creates a new Translator object
listlang = config.LANGUES
mydb = config.mydb


@bot.message_handler(commands=['start'])  # /start command
def send_welcome(message):
    mycursor = mydb.cursor()  # special object that makes requests and receives their results
    sql = "SELECT * FROM users WHERE id = %s"
    adr = (str(message.from_user.id),)
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()  # gets the result of the request made
    if myresult is None or myresult == [] or myresult == ():
        mycursor = mydb.cursor()
        sql = "INSERT INTO users (id, language) VALUES (%s, %s)"
        val = (str(message.from_user.id), "ru")
        mycursor.execute(sql, val)  # makes an INSERT query against the database using normal SQL syntax
        mydb.commit()  # when we make changes to the database - 'commit()' saves the transaction
        bot.reply_to(message, "Добро пожаловать")
    else:
        bot.reply_to(message, "Снова привет!")

    bot.reply_to(message, config.STARTMESSAGE)


@bot.message_handler(commands=['change_language'])  # /change_language command
def src_language(message):
    cid = message.chat.id
    bot.send_message(cid, config.DESTLANG, reply_markup=lang_keyboard.keyboard)


@bot.callback_query_handler(func=lambda call: True)
def dest_language(call):
    if call.data in config.LANGUES:

        language = call.data

        mycursor = mydb.cursor()
        sql = "UPDATE users SET language = %s WHERE id = %s"
        val = (language, str(call.from_user.id))

        mycursor.execute(sql, val)
        bot.send_message(call.from_user.id, 'Язык изменен на ' + config.LANGDICT[language] + '\nВведите текст')


@bot.message_handler(content_types=['text'])  # translates text of the message to selected language
def bot_trans(message):
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM users WHERE id = %s'
    adr = (message.from_user.id,)
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    language = myresult[0][1]
    trans_text = translator.translate(message.text, dest=language).text
    bot.send_message(message.from_user.id, trans_text)


if __name__ == '__main__':
    bot.polling(none_stop=True)  # tells the bot to try not to stop if any errors occur
