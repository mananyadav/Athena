def google(lur):
	"""
	searches for a specific 
	word, by opening a browser tab
	"""
	import webbrowser
	url = 'http://www.google.com/#q='
	term = lur
	webbrowser.open(url+term, new=2)