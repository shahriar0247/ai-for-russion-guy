import pyttsx3
engine = pyttsx3.init() # object creation

engine.setProperty('rate', 160)     # setting up new voice rate

engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

voices = engine.getProperty('voices')       #getting details of current voice

engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")

engine.runAndWait()
engine.stop()