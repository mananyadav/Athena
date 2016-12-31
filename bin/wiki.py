#!/usr/bin/python

def say(text):
	from gtts import gTTS
	import commands
	import os
	tts = gTTS(text=text,lang='en')
	print('\033[0;37;41m ' + text + '\033[0;37;48m ')
	tts.save('reply.mp3')
	out = 'mpg321 reply.mp3'
	a = commands.getoutput(out)

def sumUp(item):
	"""
	short two line summary of any
	wikipedia article
	"""
	import os
	import wikipedia
	import speak
	try:
		say(wikipedia.summary(item,sentences=2))
		# os.system('clear')
	except wikipedia.exceptions.DisambiguationError:
		results = wikipedia.search(item)
		os.system('clear')
		speak.speak('The closest I could find was : ' + results[1])
		print 'If this isn\'t what you were looking for then try using more keywords...'
		say(wikipedia.summary(results[1], sentences=2))
	except Exception:
		say("Couldn't find anything...")

def personUp(person):
	"""
	to find a person
	i.e. to be used when said "who is" and not "what is"
	"""
	import os
	import wikipedia
	import speak
	try:
		say(wikipedia.summary(person,sentences=2))
		# os.system('clear')
	except wikipedia.exceptions.DisambiguationError:
		results = wikipedia.search(person)
		os.system('clear')
		speak.speak('The closest I could find was : ' + results[1])
		say(wikipedia.summary(results[1],sentences=2))
	except Exception:
		say("Couldn't find anything...")