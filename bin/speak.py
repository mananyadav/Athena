def speak(tex):
	from gtts import gTTS
	import os
	tts = gTTS(text=tex,lang='en')
	tts.save('h.mp3')
	os.system('clear')
	os.system('mpg321 h.mp3')
	os.system('clear')
	
