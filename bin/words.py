#!/usr/bin/python
__author__ = 'Manan Yadav'


def main(userInput):
	"""
	the main function for the whole code
	"""
	import datetime
	import random
	from datetime import datetime
	import google
	from google import search
	import wikipedia
	import wiki
	import os
	import website
	import image
	import speak
	import music
	import maps
	import media
	import googled
	media.displayFace()
	media.badWords()
	wordDict = {}
	# userInput = raw_input('=>')
	words = userInput.split()
	a = 0
	socialNets = ['Facebook', 'Twitter', 'GitHub', 'Instagram']
	for i in words:
		wordDict[a] = i
		a += 1
	for i in range(0, len(wordDict)):
		# print pr[i]
		if wordDict[i] in ['date', 'date?']:
			speak.speak(datetime.now().strftime('Today is %d-%m-%Y'))
		elif wordDict[i] in ['Google ', 'google ']:
			speak.speak('Googling ' + userInput[i+1:] + 'or you, sir.')
		elif wordDict[i] in ['happy', 'merry', 'Happy', 'Merry']:
			speak.speak('To you too, sir.')
		elif wordDict[i] in ['bored', 'music', 'play']:
			speak.speak('Playing something for you, sir.')
			try:
				music.playMusic()
			except KeyboardInterrupt:
				print '\n'
				break
		elif wordDict[i] in socialNets:
			website.openSite(wordDict[i])
		elif wordDict[i] in ['you', 'look'] and wordDict[i] in ['there', 'alive']:
			speak.speak('For you, sir, always.')
		elif wordDict[i] in ['snap', 'picture']:
			image.takePic()
		elif wordDict[i] in ['time', ' time', 'time ', 'time?']:
			speak.speak(datetime.now().strftime('The time is %I:%M %p , sir.'))
		elif wordDict[i] in ['bye','exit']:
			speak.speak('Surely, sir.')
			quit()
		elif wordDict[i] in ['clear']:
			os.system('clear')
		elif wordDict[i] in ['cool','okay']:	
			speak.speak('Indeed.')
		elif userInput in ['hello', 'hello ']:
			greetings = {
				1: 'Hello, sir.',
				2: 'As always, nice to see you, sir.',
				3: 'Hi!',
			}
			speak.speak(greetings[random.randrange(1,4)])
		elif userInput[:8] in ['what is ']:
			Object = userInput[8:]
			wiki.sumUp(Object)
			break
		elif userInput in ['how are you', 'how is it going', "how's it going"]:
			thanks = {
				1: "I'm good. Thank you for asking, sir.",
				2: "All good, thank you.",
				3: "My systems are running pretty smothly...",
			}
			speak.speak(thanks[random.randrange(1,4)])
			break
		elif userInput[:9] in ['where is ']:
			place = userInput[9:]
			speak.speak('Finding ' + place)
			maps.place(place)
			break
		elif userInput[:8] in ['what is '] or userInput in []:
			speak.speak('Finding ' + userInput[8:])
			os.system('clear')
			print wikipedia.summary(userInput[8:],sentences=1)
			speak.speak(wikipedia.summary(userInput[8:],sentences=1))
			break
		elif userInput[:7] in ['who is ']:
			person = userInput[7:]
			speak.speak("Finding " + person)
			wiki.personUp(person)
			break
		elif userInput in ['who made you']:
			speak.speak('Manan Yadav made me.')
			break
		elif userInput[:7] in ['Google ', 'google ']:
			spam = userInput[7:]
			googled.google(spam)
			break
		elif userInput in ['name', 'who are you']:
			speak.speak("My name is Athena, sir.")
			break
