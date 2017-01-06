#!/usr/bin/python
import webbrowser

def search(arg):
	"""
	searches for people on facebook
	"""
	print 'Searching for ' + arg + '...'
	webbrowser.open('http://www.facebook.com/search/top/?q='+arg,new=2)
