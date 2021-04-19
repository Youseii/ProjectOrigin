import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import datetime
import sys


listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   #voices[1] voix femme, remplacé par 0 est c'est une voix d'homme
                                            #Problème je n'arrive pas a trouver comment ajouter une nouvelle voix
#Le volume de la voix d'origin
volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.25)

#Le débit de la voix d'origin
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            #talk('hi \nI am origin\n how can i help you ?')
            talk('Im Listening')
            print('Ecoute...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
            command = command.lower()
            if 'origin' in command:
                command = command.replace('origin', '')
                talk('Yes sir')
                print(command)
                return command
            else:
                talk('You need to say my name after the order, for example origin stop')
                # --------------(peut etre suppr) A changer car code trop long pour la boucle-------------
                print('Ecoute...')
                talk('Im Listening')
                listener.adjust_for_ambient_noise(source)
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                print(command)
                command = command.lower()
                if 'origin' in command:
                    command = command.replace('origin', '')
                    talk('Yes sir')
                    print(command)
                    return command

    except Exception as e:
        print("Exception: " + str(e))


def run_origin():
    command = take_command()

    if 'option' in command:
        listing = command.replace('option', 'play, time, google, go, joke, find and stop')
        talk('All my commands is: ' + listing)
        return command

    elif 'play' in command:
        song = command.replace('play', '')
        talk('Lets start with' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now()
        talk(time)
        print(time)

    elif 'go' in command:   # To keep have the strengh necessary to continue our project for origin :D
        true = command.replace('go', 'https://www.youtube.com/watch?v=Wo1P_OKRtcQ&list=PLRV1KoDnApTHEpj68VynYpNLcdRfpnd9B&ab_channel=MLBHighlights')
        talk("Keep em up, we can do it !")
        pywhatkit.playonyt(true)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'find' in command:
        finding = command.replace('find', '')
        results = pywhatkit.search(finding)
        print(results)
        talk('results' + finding)

    elif 'stop' in command:
        talk('Is the end')
        print(command)
        sys.exit()

    else:
        talk('I dont understand, sir')

    return command


while True:
    run_origin()
