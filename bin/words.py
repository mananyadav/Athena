#!/usr/bin/python
import datetime
from datetime import datetime
import google
from google import search
import wikipedia
import os
import speak
def main():
	running = True
	while running:
		pr = {}
		userInput = raw_input('=>')
		words = userInput.split()
		a = 0
		for i in words:
			pr[a] = i
			a += 1

		for i in range(0, len(pr)):
			# print pr[i]
			if pr[i] in ['date', 'date?']:
				speak.speak(datetime.now().strftime('Today is %d-%m-%Y'))
			elif pr[i] in ['time', 'time?']:
				speak.speak(datetime.now().strftime('The time is %H:%M %p'))
			elif pr[i] in ['exit']:
				running = False
			elif pr[i] in ['clear']:
				os.system('clear')
			# elif pr[i] == 'who':
			# 	if pr[i+1] == 'is':
			# 		person = pr[i+2:]
			# 		wikipedia.summary(person)
			elif userInput[:8] in ['what is ']:
				obg = userInput[8:]
				speak.speak('Collecting info on ' + obg + '...')
				infobg = wikipedia.summary(obg,sentences=1)
				speak.speak(infobg)
				break
			elif userInput[:7] in ['who is ']:
				person = userInput[7:]
				print 'Searching for ' + person + '...'
				infoPerson = wikipedia.summary(person,sentences=1)
				os.system('clear')
				print infoPerson
				break

if __name__ == '__main__':
	main()
