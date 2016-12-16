#!/usr/bin/python
import os
import random

a = {}
b = 0
musicList = os.listdir('../media/music/')

for i in musicList:
	a[b] = i
	b += 1

os.system ('mpg321 ../media/music/'+ a[random.randrange(0, len(musicList))])
