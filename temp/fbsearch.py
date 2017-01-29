#!/usr/bin/python
import webbrowser

def search(arg):
	print 'Searching for ' + arg + '...'
	webbrowser.open('http://www.facebook.com/search/top/?q='+arg,new=2)

inp = raw_input('Enter name : ')
search(inp)
