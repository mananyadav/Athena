#!/usr/bin/python

def takePic():
	import pygame
	import random
	import webbrowser
	import pygame.camera	
	pygame.camera.init()
	pygame.camera.list_cameras()
	cam = pygame.camera.Camera('/dev/video0',(640,480))
	cam.start()
	img = cam.get_image()
	fileName = 'img'+str(random.randrange(0,999))
	pygame.image.save(img,'media/pictures/' + str(fileName) + '.jpg')
	print ('Image saved as ' + str(fileName))
	webbrowser.open('media/pictures/'+str(fileName)+'.jpg')

# takePic()
