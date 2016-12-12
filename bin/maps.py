def place(location):
	import webbrowser
	url = 'http://www.google.com/maps/place/'
	term = location
	webbrowser.open(url+term, new=2)