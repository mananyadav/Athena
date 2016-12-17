#!/usr/bin/python
__author__ = 'Manan Yadav'
import wikipedia
import webbrowser
import os
from bin import googled
from bin import speak
from bin import	maps
import random
import speech_recognition as sr

r = sr.Recognizer()
os.system('clear')
with sr.Microphone() as source:
	os.system('clear')
	print("Listening")
	audio = r.listen(source)
try:
	userInput = r.recognize_google(audio)
	print("User : " + userInput)
	if userInput in ['hello', 'hello ']:
		greetings = {
			1: 'hello',
			2: 'hey there',
			3: 'hi!',
		}
		speak.speak(greetings[random.randrange(1,4)])
		# speak('Hey there.')
	elif userInput in ['how are you', 'how is it going', "how's it going"]:
		thanks = {
			1: "I'm good. Thanks for asking!",
			2: "All good, thank you.",
			3: "My systems are running pretty smoothly...",
		}
		speak.speak(thanks[random.randrange(1,4)])
		# speak("I am good. Thanks for asking!")
	elif userInput[:9] in ['where is ']:
		place = userInput[9:]
		speak.speak('Finding ' + place)
		maps.place(place)
	elif userInput[:8] in ['what is ']:
		speak.speak('Finding ' + userInput[8:])
		os.system('clear')
		print wikipedia.summary(userInput[8:],sentences=1)
		speak.speak(wikipedia.summary(userInput[8:],sentences=1))
	elif userInput[:7] in ['who is ']:
		speak.speak("Finding " + userInput[7:])
		os.system('clear')
		info = wikipedia.summary(userInput[7:],sentences=2)
		os.system('clear')
		text_file = open(userInput[7:]+".txt", "w")
		text_file.write(userInput[7:]+"\n")
		text_file.write(info+"\n")
		text_file.close
		infol = wikipedia.summary(userInput[7:],sentences=1)
		os.system('clear')
		print infol
		speak.speak(infol)
	elif userInput in ['who made you']:
		speak.speak('Manan Yadav made me.')
	elif userInput[:7] in ['Google ']:
		spam = userInput[7:]
		googled.google(spam)
	elif userInput in ['name', 'who are you']:
		speak.speak("My name is Athena")
	elif userInput in ['sleep', 'bye bye', 'exit']:
		speak.speak("Bye")
		exit()
except sr.UnknownValueError:
	speak.speak("")

os.system('python athena.py')
