import speech_recognition as sr
import pyttsx3

def say(say):
    engine = pyttsx3.init() # object creation
    engine.setProperty('rate', 160)     # setting up new voice rate
    engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
    engine.say(say)
    engine.runAndWait()
    engine.stop()
    print(say)


say("Hello, my name is Aygerim. I am an artificial intelligence. I am here to make an order. From which city are you from, and what is your address?")

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something")
    audio = r.listen(source)

said = r.recognize_google(audio)
said = said.lower()

say("Thank you very much. So you are from " + said + " and what would you like to order?")

address = said
with sr.Microphone() as source:
    print("Say Something")
    audio = r.listen(source)

said = r.recognize_google(audio)
said = said.lower()

say("So you are ordering " + said + " am i right?")
order = said

with sr.Microphone() as source:
    print("Say Something")
    audio = r.listen(source)

said = r.recognize_google(audio)
said = said.lower()

if said == "yes":
    say("Thank you very much")
if said == "no":
    say("Please repeat the whole order")