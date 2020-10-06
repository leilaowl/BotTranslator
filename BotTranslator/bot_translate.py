# this file is to demonstrate how translation works

# Googletrans is a free and unlimited python library that implemented Google Translate API
from googletrans import Translator

translator = Translator()
# print(translator.translate(message, dest='ru'))

while True:
    message = input('')
    result = translator.translate(message, dest='ru')
    print(result.text)
