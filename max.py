import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
 engine.say(text)
 engine.runAndWait()
 
def take_command():
    try:
        with sr.Microphone() as source:
            talk('Hey, I am Max, your virtual assistant, what can I do for you?')
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'max' in command:
                command=command.replace('max','')
                print(command)  
            elif 'max' not in command:
                talk('Please say a valid command and try again')
                sys.exit(2)
    except SystemExit:
        sys.exit(2)
    except:
        sys.exit(2)
    return command

def run_max():
    try:
        command = take_command()
        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(time)
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'search' in command:
            to_serach = command.replace('search', '')
            talk('seacrhing' + to_serach)
            pywhatkit.search(to_serach)
        elif 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)    
            talk('Now the time is' + time)
        elif 'who is' or 'what is' in command:
            to_check = command.replace('what is', '')
            to_check = command.replace('who is', '')
            info = wikipedia.summary(to_check, 2)
            talk('From wikipedia, ' + info)
        elif 'quit' in command:
            sys.exit(2)
        else:
            talk('Please say a valid command and do try again')
    except SystemExit:
        sys.exit(2)
    except:
        sys.exit(2)

while True:
    run_max()