# ------------------------------------------------------------------------------
# Imports
import googletrans
from googletrans import *
import pyttsx3

# ------------------------------------------------------------------------------
# Setup
translator = googletrans.Translator()
# translator = Translator()
# ------------------------------------------------------------------------------
# Part 1:
translate = translator.translate('Hello There How Are You', dest='korean')
print(translate.text)

# ------------------------------------------------------------------------------
# Part 2:
print(translator.detect('이 문장은 한글로 쓰여졌습니다'))

# ------------------------------------------------------------------------------
# Part 3:

input_text = input('Input Your Translation Text : ')
input_language = input('Input Your Translation Language : ')

translation = translator.translate(input_text, dest=input_language)
print(translation.text)
# ------------------------------------------------------------------------------
# Part 4:
#
speaker = pyttsx3.init()
translate_speech = translator.translate('Hello There How Are You', dest='spanish')

speaker.say(translate_speech.text)
speaker.runAndWait()

# ------------------------------------------------------------------------------
