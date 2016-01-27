import pyttsx

engine = pyttsx.init()

#Sets error values
errora = 'You are viewing this on a non FLur system.'
errorb = 'It is not meant to be viewed on a non FLur system.'

#Print error values to inform that they are running it on a non FLur system
print(errora)
print(errorb)

#Magic TTS
engine.say('This is a test for the FLur Hub.')
engine.say('If you hear this, the speakers are working.')
engine.say('Next the Microphone will be configured.')

engine.runAndWait()
