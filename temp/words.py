#!/usr/bin/python
import webbrowser
import wikipedia
def google(link):
	url = 'http://www.google.com/#q=' + link
	webbrowser.open(url,2)
	print ''
pr = {}
userInput = raw_input('-->')
words = userInput.split()
a = 0
for i in words:
	pr[a] = i
	a += 1

# print pr[1]
#print pr
for i in range(0, len(pr)):
	if pr[i] == 'google':
		google(pr[i+1])
	elif pr[i] == 'who':
		if pr[i+1] == 'is':
			wikipedia.summary(pr[i+2], sentences=2)
		
exit()
