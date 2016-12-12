#!/usr/bin/python
import os
import pyttsx
import speech_recognition as sr

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-24)
#engine.say('')
#engine.runAndWait()
#engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
	print("Say something!")
	audio = r.listen(source)

try:
	print("User : " + r.recognize_google(audio))
	if r.recognize_google(audio) in ['hello', 'Hello', 'hello ']:
		print("Nice to meet you!")
		engine.say("Hello! Nice to meet you!")
		engine.runAndWait()
	elif r.recognize_google(audio) in ['name', 'name ']:
		print("John")
		engine.say("My name is John")
		engine.runAndWait()
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
