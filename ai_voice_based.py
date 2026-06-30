import pyttsx3
import datetime
import time

def speak(audiovoice):
    print(audiovoice)

    engine = pyttsx3.init()
    engine.say(audiovoice)
    engine.runAndWait()
    engine.stop()

def greet():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 11:
        speak("Good Morning Sir")
    elif hour >= 11 and hour < 15:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")

    time.sleep(1)
    speak("I am your personal assistant")

speak("Hello Brother")

greet()