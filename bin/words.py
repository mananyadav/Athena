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

for i in range(0, len(pr)):
	# print pr[i]
	if pr[1] == 'time':
		
exit()
