#!/usr/bin/python

from gtts import gTTS
import os

dir_file = open('/home/user/Desktop/speech.txt', 'r')
text = dir_file.read()
dir_file.close()

tts = gTTS(text=text, lang='en')
tts.save('speech.mp3')
print text
os.system('mpg321 speech.mp3')
