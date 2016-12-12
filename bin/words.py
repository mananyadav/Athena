#!/usr/bin/python
import datetime
import random
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
				speak.speak(datetime.now().strftime('The time is %I:%M %p'))
			elif pr[i] in ['exit']:
				running = False
			elif pr[i] in ['clear']:
				os.system('clear')
			# elif pr[i] == 'who':
			# 	if pr[i+1] == 'is':
			# 		person = pr[i+2:]
			# 		wikipedia.summary(person)
			elif userInput in ['hello', 'hello ']:
				greetings = {
					1: 'hello',
					2: 'hey there',
					3: 'hi!',
				}
				speak.speak(greetings[random.randrange(1,4)])
			elif userInput[:8] in ['what is ']:
				obg = userInput[8:]
				speak.speak('Collecting info on ' + obg + '...')
				infobg = wikipedia.summary(obg,sentences=1)
				speak.speak(infobg)
				break
			elif userInput in ['how are you', 'how is it going', "how's it going"]:
				thanks = {
					1: "I'm good. Thanks for asking!",
					2: "All good, thank you.",
					3: "My systems are running pretty smoothly...",
				}
				print(thanks[random.randrange(1,4)])
				break
			elif userInput[:9] in ['where is ']:
				place = userInput[9:]
				speak.speak('Finding ' + place)
				speak.place(place)
				break
			elif userInput[:8] in ['what is ']:
				speak.speak('Finding ' + userInput[8:])
				os.system('clear')
				print wikipedia.summary(userInput[8:],sentences=1)
				speak.speak(wikipedia.summary(userInput[8:],sentences=1))
				break
			elif userInput[:7] in ['who is ']:
				speak.speak("Finding " + userInput[7:])
				os.system('clear')
				info = wikipedia.summary(userInput[7:],sentences=2)
				os.system('clear')
				text_file = open(userInput[7:]+".txt", "w")
				text_file.write(userInput[7:]+"\n")
				text_file.write(info+"\n")
				text_file.close()
				infol = wikipedia.summary(userInput[7:],sentences=1)
				os.system('clear')
				print(infol)
				speak.speak(infol)
				break
			elif userInput in ['who made you']:
				speak.speak('Manan Yadav made me.')
				break
			elif userInput[:7] in ['Google ']:
				spam = userInput[7:]
				googled.google(spam)
				break
			elif userInput in ['name', 'who are you']:
				speak.speak("My name is Jewl")
				break	

if __name__ == '__main__':
	main()
