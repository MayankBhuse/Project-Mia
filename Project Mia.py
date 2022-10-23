from datetime import datetime
from socket import if_nameindex, if_nametoindex
from pip import main
from sys import exit


import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import pyautogui
import pyjokes



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(): # Wish Function

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Master!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Master!")   

    else:
        speak("Good Evening Master!")     

    speak("I am Mia. Please tell me how may i help you")
    
def takeCommand(): # It takes microphone command from the user and returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        print(f" User said: {query}")    

    except Exception as e:
        #print(e)
        speak("Say that again please...")
        return "None"
    return query

def music():
    speak("Tell me name of song you want to listen sir ")
    musicname = takeCommand()

    if 'alcholia' in musicname:
        os.startfile('C\\Songs')
    else:    
        pywhatkit.playonyt(musicname)
        speak(" Your songs has been started, enjoy sir !")
     
if __name__ == "__main__":
    wishMe()
    
    while True: # Logic for executing tasks based on query
        #if 1:
        query = takeCommand().lower()
        print(" query "+query)
        
        if 'hello' in query: # Hello command when A.I Started
            speak('Hello sir...')

        elif 'goodbye' in query: # Goodbye command when A.I Stopped
            speak(" The system will catch you later, sir. ")
            exit(0)

        elif 'exit' in query: # Goodbye command when A.I Stopped
            speak(" The system will catch you later, sir. ")
            exit(0)            
        
        elif 'time' in query: # Time when asked
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif 'youtube' in query: # Youtube when asked
            speak(" Ok sir, This is what i found for your search ! ")
            query = query.replace("Mia","")
            query = query.replace ("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Done sir")

        elif 'google' in query: # Google when asked
            speak(" Ok sir, This is what i found for your search ! ")
            query = query.replace("Mia","")
            query = query.replace ("google search","")
            pywhatkit.search(query)
            speak("Done sir")       

        elif 'website' in query: # Website when asked
            speak(" Ok sir, This is what i found for your search ! Launching.... ")
            query = query.replace("Mia","")
            query = query.replace ("website","")
            web1 = query.replace("open","")
            web2 = "https://www." + web1 + 'com'
            webbrowser.open(web2)
            speak("Done sir")            

        elif 'launch' in query: # launch any website when asked
            speak(" Sir tell me the name of website! ")
            name = takeCommand()
            web = "https://www." + name + 'com'
            webbrowser.open(web)
            speak("Done sir")            

        elif 'music' in query: # lauch music
            music()

        elif 'wikipedia' in query: # lauch wikipedia and search
            speak('searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)
  
        elif 'screenshot' in query: # take screenshot
            kk = pyautogui.screenshot()
            kk.save('C:\\Users\Jstmanku\\Pictures\\')

        elif 'repeat my words' in query: # text to speech
            speak(" You may start to speak sir !")
            jj = takeCommand()
            speak(f" You said : {jj}")

        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)
            

       
        





