import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()  # this function will recognize my voice
engine = pyttsx3.init()  # this function converts text to speech
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # this converts male voice into female
text = "HELLO ROJESH!! How are you?"


def talk(text):  # Alexa speaks with me
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:  # my voice will be the source
            print('Listening.....')
            voice = listener.listen(source)  # my voice will be stored in voice variable
            command = listener.recognize_google(
                voice)  # using google, API my voice will be recognized. Voice to Text translation
            command = command.lower()
            print(command)
    except:
        print("Error")
        exit()
    return command


def run_alexa():
    print(text)
    command = take_command()

    command = command.lower()
    print(command)
    if 'play' in command:
        command = command.replace('play', '')
        talk(f'Playing {command}')
        print(f"Playing {command}")
        pywhatkit.playonyt(command)

    elif 'single' in command:
        talk("Chup bey bhhosdeekay.")
        talk("I have a boyfriend.")

    elif 'time' in command:
        time = datetime.datetime.now().strftime(
            '%I:%M %p')  # This gives the string form of time right now. I is the 12 hour format whereas H gives the 24 hour format and p gives whether AM or Pm. We can add S to givce seconds
        print(time)
        talk("Current Time is " + time)

    elif 'search' or 'find' or 'define' in command:
        person = command.replace('search', '')
        info = wikipedia.summary(person, 2)  # gives 2 line summary of the searched thing
        print(info)
        talk(info)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)

    elif 'exit' in command:
        exit()

    else:
        talk("Please say the command again!")


while True:
    talk(text)
    run_alexa()
