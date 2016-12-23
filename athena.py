#!/usr/bin/python
__author__ = 'Manan Yadav'
import wikipedia
import webbrowser
import os
from bin import googled
from bin import speak
from bin import	maps
from bin import words
import random
import speech_recognition as sr

words = sr.Recognizer()
os.system('clear')
with sr.Microphone() as source:
	os.system('clear')
	print("Listening")
	audio = words.listen(source)
try:
	userInput = words.recognize_google(audio)
	print("User : " + userInput)
	words.main(userInput)
except sr.UnknownValueError:
	speak.speak("")

os.system('python athena.py')
