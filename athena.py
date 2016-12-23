#!/usr/bin/python
__author__ = 'Manan Yadav'

def main():
	import os
	from bin import words
	import speak
	import speech_recognition as sr

	word = sr.Recognizer()
	os.system('clear')
	with sr.Microphone() as source:
		os.system('clear')
		print("Listening")
		audio = word.listen(source)
	try:
		from bin import words
		userInput = word.recognize_google(audio)
		print("User : " + userInput)
		words.main(str(userInput))
	except sr.UnknownValueError:
		pass

	os.system('python athena.py')

if __name__ == '__main__':
	main()