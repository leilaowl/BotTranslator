# project configuration
import pymysql  # pymysql to use databases


TOKEN = '1306009172:AAHBydmhQ7vV1aAh54Cd7rbDEMH7VfxMq2s'
STARTMESSAGE = '''
    Я помогу тебе с переводом. \nЯ автоматически расспознаю язык, который ты вводишь.\
    Тебе остается только выбрать язык перевода!\
    /change_language - комманда, чтобы выбрать\\сменить язык\
    Успехов!'''
DESTLANG = 'На какой язык сделать перевод?'
LANGUES = ['ru', 'de', 'en', 'uk', 'he', 'zh-cn', 'fr']
LANGDICT = {
    'ru': 'Русский',
    'de': 'Немецкий',
    'en': 'Английский',
    'uk': 'Украинский',
    'he': 'Иврит',
    'zh-cn': 'Китайский(упр)',
    'fr': 'Французский'
}

mydb = pymysql.connect(
    host='db4free.net',
    port=3306,
    user='leilaowl',
    passwd='sql2824leila',
    database='bottranslator'
)
