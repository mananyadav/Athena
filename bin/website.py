#!/usr/bin/python

def openSite(url):
	"""
	simply opens the desired 
	website, easy.
	"""
	import webbrowser
	webbrowser.open('http://www.' + url + '.com', 2)