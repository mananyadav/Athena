#!/usr/bin/python
import wikipedia
import pyttsx

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',rate-30)

searchItem = raw_input("What are you curious about today?\n->")
info = wikipedia.summary(searchItem, sentences=2)

print info
engine.say(info)
engine.runAndWait()
