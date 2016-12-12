#!/usr/bin/python
import datetime
from datetime import datetime
import datetime
import wikipedia

pr = {}
userInput = raw_input('-->')
words = userInput.split()
a = 0
for i in words:
	pr[a] = i
	a += 1

for i in range(0, len(pr)):
	# print pr[i]
	if pr[i] in ['date', 'date?']:
		today = datetime.date.today()
		print today.strftime('The date is %d, %b %Y')
	elif pr[i] in ['time', 'time?']:
		print datetime.now().strftime('%H:%M %p')
	# elif pr[i] == 'who':
	# 	if pr[i+1] == 'is':
	# 		person = pr[i+2:]
	# 		wikipedia.summary(person)
	# elif userInput[:7] in ['who is ']:
	#	person = userInput[7:]
	#	print 'Searching for ' + person + '...'
	#	infoPerson = wikipedia.summary(person,sentences=1)
	#	print infoPerson
exit()