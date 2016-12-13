def speak(tex):
	from gtts import gTTS
	import commands
	import os
	tts = gTTS(text=tex,lang='en')
	print tex
	tts.save('reply.mp3')
	out = 'mpg321 reply.mp3'
	a = commands.getoutput(out)
	# os.system('mpg321 h.mp3')
