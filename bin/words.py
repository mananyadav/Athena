#!/usr/bin/python
import datetime
from datetime import datetime
import wikipedia
import os
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
				print datetime.now().strftime('Today is %d-%m-%Y')
			elif pr[i] in ['time', 'time?']:
				print datetime.now().strftime('The time is %H:%M %p')
			elif pr[i] in ['exit']:
				running = False
			elif pr[i] in ['clear']:
				os.system('clear')
			# elif pr[i] == 'who':
			# 	if pr[i+1] == 'is':
			# 		person = pr[i+2:]
			# 		wikipedia.summary(person)
			elif userInput[:7] in ['who is ']:
				person = userInput[7:]
				print 'Searching for ' + person + '...'
				infoPerson = wikipedia.summary(person,sentences=1)
				os.system('clear')
				print infoPerson
				break

if __name__ == '__main__':
	main()
