#!/usr/bin/python
def playMusic():
	"""
	simple script to get the music files from the media/music folder
	and then play the files...
	supports only mp3 
	"""
	import os
	import random
	import commands

	a = {}
	b = 0
	musicList = os.listdir('../media/music/')

	for i in musicList:
		a[b] = i
		b += 1

	commands.getoutput('mpg321 ../media/music/'+ a[random.randrange(0, len(musicList))])