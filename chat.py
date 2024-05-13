import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import cv2
import pyjokes
import smtplib


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#print(f"jarvis : {audio}
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Night!")

    speak("Hello Mam! I am jarvis. how can i assist you?")

def takecommand():
    
    r = sr.Recognizer()
    with sr .Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("recognizing...")
            query = r.recognize_google(audio, language="en-in")            
            print(f"user said: {query}\n")


        except Exception as e:
            print(e)

            print("say that again please...")
            return "None"
        return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('username@gmail.com', 'password')
    server.sendmail('username@gmail.com', to, content)
    server.close()
    
if __name__ == "__main__":
    wishMe()
    while True:
        #if 1:
        query = takecommand().lower()
        
        #logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
   
        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strtime}")
            
        elif 'open code' in query:
         codePath ="C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codePath)

        elif 'play music' in query:
            music_dir ="D:\\songs\\favorite songs"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open notepad' in query:
            npath ="C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
        
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True: 
                ret, img = cap.read()
                cv2.imshow('camera', img)
                k= cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
    
        elif 'email to Prachi' in query:
         try:
                speak("what should i say?")
                content = takecommand()
                to = "username@gmail.com"
                sendEmail(to, content)
                speak("email has been sent!")
         except Exception as e: 
                print(e)
                speak("sorry! I am not able to send this email")
                



