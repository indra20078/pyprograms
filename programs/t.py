import pywhatkit
import pyttsx3
import speech_recognition as sr

def a(): 
    r = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            print("Recognising...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said:{query}")
            a = query.replace('play', '')
            pywhatkit.playonyt(a)
    except :
        pass
takeCommand()
