#Requirements for the projects are pyttsx3,speech_recognition,date_time and pyaudio module

import pyttsx3
import speech_recognition as sr
import datetime
import time

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audiovoice):
    # engine.say("Hellow Abhijeet")
    print(audiovoice)
    engine.say(audiovoice)
    engine.runAndWait()


def takevoiceCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold=1
        try:
            audio=r.listen(source,timeout=30,phrase_time_limit=10)
            print("Listening your voice please wait...")
            text=r.recognize_google(audio,language='en-in')
            return text

        except Exception as e:
            speak("Unable to recognize your voice")
            return ""

def greet():
    hour=int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour<11:
        speak("Good Morning Sir")

    elif hour>=11 and hour<15:
        speak("Good afternoon sir")
    elif hour>=15 and hour<24:
        speak("Good evening sir")

    time.sleep(0.5)
    speak("I am your personal assistant")







speak("Hellow Brother")

greet()


    # while True:
    #     work=takevoiceCommand().lower()
    #     if 'hello' in work:
    #         speak('I am fine. Thank you for asking')
    #     elif 'bye' in work:
    #         speak('bye Sir... See you again another time')
    #         exit()
