#!/usr/bin/python
import wikipedia
import webbrowser
import os
from bin import googled
from bin import speak
import random
import speech_recognition as sr

__author__ = 'manan'

def place(location):
	url = 'http://www.google.com/maps/place/'
	term = location
	webbrowser.open(url+term, new=2)

r = sr.Recognizer()
os.system('clear')
with sr.Microphone() as source:
	os.system('clear')
	print("Listening")
	audio = r.listen(source)
try:
	goog = r.recognize_google(audio)
	print("User : " + goog)
	if goog in ['hello', 'hello ']:
		greetings = {
			1: 'hello',
			2: 'hey there',
			3: 'hi!',
		}
		speak.speak(greetings[random.randrange(1,4)])
		# speak('Hey there.')
	elif goog in ['how are you', 'how is it going', "how's it going"]:
		thanks = {
			1: "I'm good. Thanks for asking!",
			2: "All good, thank you.",
			3: "My systems are running pretty smoothly...",
		}
		speak.speak(thanks[random.randrange(1,4)])
		# speak("I am good. Thanks for asking!")
	elif goog[:9] in ['where is ']:
		place = goog[9:]
		speak.speak('Finding ' + place)
		speak.place(place)
	elif goog[:8] in ['what is ']:
		speak.speak('Finding ' + goog[8:])
		os.system('clear')
		print wikipedia.summary(goog[8:],sentences=1)
		speak.speak(wikipedia.summary(goog[8:],sentences=1))
	elif goog[:7] in ['who is ']:
		speak.speak("Finding " + goog[7:])
		os.system('clear')
		info = wikipedia.summary(goog[7:],sentences=2)
		os.system('clear')
		text_file = open(goog[7:]+".txt", "w")
		text_file.write(goog[7:]+"\n")
		text_file.write(info+"\n")
		text_file.close
		infol = wikipedia.summary(goog[7:],sentences=1)
		os.system('clear')
		print infol
		speak.speak(infol)
	elif goog in ['who made you']:
		speak.speak('Manan Yadav made me.')
	elif goog[:7] in ['Google ']:
		spam = goog[7:]
		googled.google(spam)
	elif goog in ['name', 'who are you']:
		speak.speak("My name is Athena")
	elif goog in ['sleep', 'bye bye', 'exit']:
		speak.speak("Bye")
		exit()
except sr.UnknownValueError:
	speak.speak("")

os.system('python athena.py')
