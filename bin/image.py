#!/usr/bin/python


def takePic():
	"""
	takes a picture
	from the first webcam
	detected
	"""
	import pygame
	import random
	import webbrowser as web
	import pygame.camera	
	pygame.camera.init()
	pygame.camera.list_cameras()
	cam = pygame.camera.Camera('/dev/video0',(640,480))
	cam.start()
	img = cam.get_image()
	fileName = 'img'+str(random.randrange(0,999))
	pygame.image.save(img,'media/pictures/' + str(fileName) + '.jpg')
	print ('Image saved as ' + str(fileName))
	web.open('media/pictures/'+str(fileName)+'.jpg')

# takePic()
