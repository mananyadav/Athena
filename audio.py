#!/usr/bin/python
import wikipedia
import webbrowser
import os
import random
from gtts import gTTS
import speech_recognition as sr

def googl(lur):
	url = 'http://www.google.com/#q='
	term = lur
	webbrowser.open(url+term, new=2)

def speak(tex):
	tts = gTTS(text=tex,lang='en')
	tts.save('h.mp3')
	os.system('clear')
	os.system('mpg321 h.mp3')
	os.system('clear')

r = sr.Recognizer()

with sr.Microphone() as source:
	print("Say something!")
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
		speak(greetings[random.randrange(1,4)])
		# speak('Hey there.')
	elif goog in ['how are you']:
		speak("I am good. Thanks for asking!")
	elif goog[:8] in ['what is ']:
		speak('Finding ' + goog[8:])
		os.system('clear')
		print wikipedia.summary(goog[8:],sentences=1)
		speak(wikipedia.summary(goog[8:],sentences=1))
	elif goog[:7] in ['who is ']:
		speak("Finding " + goog[7:])
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
		speak(infol)
	elif goog in ['who made you']:
		speak('Manan Yadav made me.')
	elif goog in ['']:
		speak('Alarm set.')
	elif goog[:7] in ['Google ']:
		spam = goog[7:]
		googl(spam)
	elif goog in ['name', 'name ', 'who are you']:
		speak("My name is Jewl")
	elif goog in ['sleep', 'bye', 'exit']:
		speak("Bye")
		exit()
except sr.UnknownValueError:
	speak("Couldn't understand")

os.system('python audio.py')
