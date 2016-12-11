#!/usr/bin/python
import wikipedia
from gtts import gTTS

searchItem = raw_input('Enter query = ')
info = wikipedia.summary(searchItem, sentences=2)

text_file = open(searchItem+'.txt', "w")
text_file.write(searchItem+"\n")
text_file.write(info+"\n")
text_file.close
