def place(location):
	"""
	finds out location of a place 
	uses google maps 
	GUI only... :(
	"""
	import os
	import webbrowser
	url = 'http://www.google.com/maps/place/'
	term = location
	webbrowser.open(url+term, new=2)
	os.system('clear')