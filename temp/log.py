#!/usr/bin/python

a = True
while a:
	inp = str(raw_input('-->'))
	if inp in ['exit']:
		fo.close()
		a = False
	fo = open('save.txt', 'a')
	fo.write(inp+'\n')	

exit()

