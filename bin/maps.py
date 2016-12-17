def place(location):
	"""
	finds out location of a place 
	uses google maps 
	GUI only... :(
	"""
	import webbrowser
	url = 'http://www.google.com/maps/place/'
	term = location
	webbrowser.open(url+term, new=2)