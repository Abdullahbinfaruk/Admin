import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
meena = pyttsx3.init()
voices = meena.getProperty('voices')
meena.setProperty('voice', voices[1].id)


def talk(text):
    meena.say(text)
    meena.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            meena.say("Welcome")
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'meena' in command:
                command = command.replace('meena', '')
    except:
        pass
    return command



def run_meena():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('I did not get it but I am going to search it for you')
        pywhatkit.search(command)


while True:
    run_meena()