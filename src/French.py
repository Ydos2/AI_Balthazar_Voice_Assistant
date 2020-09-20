import re
import platform
import os
import time
import datetime
from .website import websiteText

def FrenchFunction(Balthazar, text, languages):
    websiteText(Balthazar, text, languages)

    if "Bonjour" in text:
        Balthazar.speak("bonjour, comment allez vous?", languages)

    elif "au revoir" in text:
        Balthazar.speak("Au revoir Maître", languages)
        return 84

    if "qui es-tu" in text:
        Balthazar.speak("Je suis Balthazar, un logiciel d'assistance vocale créé par Mathias Ressort", languages)

    elif "langue" in text:
        if "français" in text:
            languages = 1
            Balthazar.speak("J'ai changer la langue en Français", languages)
        else:
            languages = 0
            Balthazar.speak("I change the language in English", languages)

    elif "quel est ton nom" in text:
        Balthazar.speak("Mon nom est Balthazar", languages)

    elif 'joue de la musique' in text:
        music_dir = './'  #Your Path
        songs = os.listdir(music_dir)
        print(songs)    
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'heure' in text:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        Balthazar.speak(f"Monsieur, il est {strTime} heure", languages)

    else:
        Balthazar.speak("Désolé, je ne comprends pas mon maître", languages)
    
    return languages