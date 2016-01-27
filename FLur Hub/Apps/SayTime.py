import pyttsx
from datetime import datetime

engine = pyttsx.init()

#Sets error values
errora = 'You are viewing this on a non FLur system.'
errorb = 'It is not meant to be viewed on a non FLur system.'

#Print error values to inform that they are running it on a non FLur system
print(errora)
print(errorb)

#Say the time in 24 hour format.
engine.say('The current time is')
engine.say(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
engine.runAndWait()

