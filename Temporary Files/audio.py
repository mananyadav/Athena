#!/usr/bin/python

from gtts import gTTS
import os

inp = raw_input("=>")

tts = gTTS(text=inp, lang='en')
tts.save('hello.mp3')
os.system('mpg321 hello.mp3')

