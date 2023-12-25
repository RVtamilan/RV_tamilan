import wikipedia 
result = wikipedia.summary("sundar pichai",sentences = 2)
print(result)
from pyttsx3 import *
engine = init()
engine.setProperty('rate',150)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[11].id)
engine.say(result)
engine.runAndWait()
engine.stop()
