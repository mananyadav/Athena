def google(lur):
	import webbrowser
	url = 'http://www.google.com/#q='
	term = lur
	webbrowser.open(url+term, new=2)