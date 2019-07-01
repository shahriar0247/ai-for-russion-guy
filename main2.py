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

def ask():
    r = sr.Recognizer()
    print("say something")
    
    with sr.Microphone() as source:
        audio = r.listen(source)
    said = r.recognize_google(audio)
    said = said.lower()
    return said

say("Привет. Меня зовут Айгерим. Я искусственный интеллект. Я здесь, чтобы помочь вам сделать заказ. Из какого ты города и по какому адресу?")

said = ask()

say("Большое спасибо. Итак, вы из " + said + " а что бы вы хотели заказать?")

address = said

said = ask()

say("Итак, вы заказываете" + said + " я прав")
order = said

said = ask()

if said == "да":
    say("Большое спасибо за выбор KFC. Ваш заказ будет доставлен в течение полутора часов. Спасибо")
if said == "нет":
    say("Пожалуйста, повторите весь заказ")