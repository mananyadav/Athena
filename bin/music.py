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
	songs = {}
	spam = 0
	musicList = os.listdir('media/music/')
	if len(musicList) == 0:
		print 'You need to place readable music files in the media/music directory!'
	else:
		for i in musicList:
			songs[spam] = i
			spam += 1
		commands.getoutput('mpg321 media/music/'+ songs[random.randrange(0, len(musicList))])
