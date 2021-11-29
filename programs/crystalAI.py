import pyttsx3
import datetime
import pywhatkit
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[-1].id)
engine. setProperty("rate", 130)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 16:
        speak("Good afternoon")
    else:
        speak("Good Evening")
    speak("This is crystal, How may i help you")
    
def send_email(content):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('primemember248@gmail.com','123qwe@456rty')
    server.sendmail('primember248@gmail.com',
                 'indradhanushhs@gmail.com',
                  content)

    server.quit()
def takeCommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
wish()
while True:
    query = takeCommand().lower()

    if "wikipedia" in query:
        print("Searching wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif "open" in query:
        list(query)
        web,web1 = query.split()
        web1 = web1.lower()
        web1 = web1 +".com"
        webbrowser.open(web1)
    elif "time" in query:
        hour = int(datetime.datetime.now().hour)
        print(hour)
        speak(hour)
    elif "play" in query: 
        a = query.replace('play', '')
        pywhatkit.playonyt(a)

        
    elif "email" in query:
        try:  
            speak("What should i say??")
            a = takeCommand()
            send_email(a)
            print("Your email has been sent")
            speak("Your email has been sent")
        
        except Exception as e:
            print(e)      