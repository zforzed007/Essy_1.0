

from tkinter import N
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<17:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("My name is Essy! How may I help you")

def takecommand():
    #takes input and gives output
   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 800
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    
    except Exception as e:
        print(e)
        speak("Could you please repeat")
        print("Could you please repeat")
        return "None"
    return query
        
def closeapps():
    speak(f"closing {query}")
    if 'spotify' in query:
        os.system("TASKKILL /f /im spotify.exe")
        
    elif 'discord' in query:
        os.system("TASKKILL /f /im discord.exe")
        
    elif 'steam' in query:
        os.system("TASKKILL /f /im steam.exe")
        
    #elif 'hotstar' in query:
        #os.system("TASKKILL /f /im app.exe")    
    
    elif 'code' in query:
        os.system("TASKKILL /f /im code.exe")
        
    elif 'vmware' in query:
        os.system("TASKKILL /f /im vmplayer.exe")

if __name__=="__main__":
    wishme()
    while True:
    
        query = takecommand().lower()
        #logic for execution
        
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'who are you' in query:
            print("I am a voice assistant...my name is Essy")
            speak("I am a voice assistant...my name is Essy")
        
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com") 
            
        elif 'search on youtube' in query:
            query = query.replace("search on youtube","")
            speak(f"searching {query} on youtube")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            
        elif 'search on google' in query:
            query = query.replace("search on google","")
            speak(f"searching {query} on google")
            pywhatkit.search(query) 
        
        elif 'open website' in query:
            query = query.replace("open website","")
            query = query.replace(" ","")
            speak(f"opening {query} .com ")
            web = 'https://www.' + query + '.com'
            webbrowser.open(web)
        
        elif 'open mail' in query:
            speak("Opening gmail")
            webbrowser.open("gmail.com")
            
        elif 'open map' in query:
            speak("Opening maps")
            webbrowser.open("googlemaps.com") 
         
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
        
        elif 'open discord' in query:
            speak("Opening discord")
            codePath = "C:\\Users\\Z\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord"
            os.startfile(codePath)
            
        elif 'open code' in query:
            speak("Opening vs code")
            codePath = "C:\\Users\\Z\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code"
            os.startfile(codePath)   
            
        elif 'open steam' in query:
            speak("Opening steam")
            codePath = "D:\\programs\\Steam\\steam"
            os.startfile(codePath)
            
        elif 'open vmware' in query:
            speak("Opening VM ware")
            codePath = "C:\\Program Files (x86)\\VMware\\VMware Player\\vmplayer"
            os.startfile(codePath)
            
        elif 'open spotify' in query:
            speak("Opening spotify")
            codePath = "C:\\Users\\Z\\OneDrive\\Desktop\\Spotify"
            os.startfile(codePath)  
            
        elif 'open hotstar' in query:
            speak("Opening hotstar")
            codePath = "C:\\Users\\Z\\OneDrive\\Desktop\\Hotstar"
            os.startfile(codePath)    
    
        elif 'close app' in query:
            query = query.replace("close app","")
            closeapps()           
        
        elif 'quit' in query:
            speak("terminating")
            exit(0)
             
        