import re
import platform
import os
import time
import datetime
from .website import websiteText

def EnglishFunction(Balthazar, text, languages):
    websiteText(Balthazar, text, languages)

    if "hello" in text:
        Balthazar.speak("hello, how are you?", languages)

    elif "goodbye" in text:
        Balthazar.speak("Goodbye Master", languages)
        return 84

    if "who are you" in text:
        Balthazar.speak("I am Balthazar, a voice assistance software created by Mathias Ressort", languages)

    elif "language" in text:
        if "French" in text:
            languages = 1
            Balthazar.speak("J'ai changer la langue en Français", languages)
        else:
            languages = 0
            Balthazar.speak("I change the language in English", languages)

    elif "what is your name" in text:
        Balthazar.speak("My name is Balthazar", languages)

    elif 'play music' in text:
        music_dir = './'  #Your Path
        songs = os.listdir(music_dir)
        print(songs)    
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'time' in text:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        Balthazar.speak(f"Sir, the time is {strTime}", languages)

    else:
        Balthazar.speak("Sorry, i don't understand my master", languages)
    
    return languages