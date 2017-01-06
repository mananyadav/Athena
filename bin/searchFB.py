#!/usr/bin/python

def search(arg):
	"""
	searches for people on facebook
	"""
	import webbrowser
	print 'Searching for ' + arg + '...'
	webbrowser.open('http://www.facebook.com/search/top/?q='+arg,new=2)
