#!/usr/bin/python

def sumUp(item):
	"""
	short two line summary of any
	wikipedia article
	"""
	import os
	import wikipedia
	import speak
	try:
		speak.speak(wikipedia.summary(item,sentences=2))
		# os.system('clear')
	except wikipedia.exceptions.DisambiguationError:
		results = wikipedia.search(item)
		os.system('clear')
		speak.speak('The closest I could find was : ' + results[1])
		print 'If this isn\'t what you were looking for then try using more keywords...'
		speak.speak(wikipedia.summary(results[1], sentences=2))
	except Exception:
		speak.speak("Couldn't find anything...")

def personUp(person):
	"""
	to find a person
	i.e. to be used when said "who is" and not "what is"
	"""
	import os
	import wikipedia
	import speak
	try:
		speak.speak(wikipedia.summary(person,sentences=2))
		# os.system('clear')
	except wikipedia.exceptions.DisambiguationError:
		results = wikipedia.search(person)
		os.system('clear')
		speak.speak('The closest I could find was : ' + results[1])
		speak.speak(wikipedia.summary(results[1],sentences=2))
	except Exception:
		speak.speak("Couldn't find anything...")