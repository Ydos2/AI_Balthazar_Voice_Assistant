import os
import time
import datetime
import json
from src.website import website_text
from src.Class_Bathazar import Balthazar_Class

def Welcome(Balthazar):
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        Balthazar.speak("Good Morning!", 0)
    elif hour >= 12 and hour < 18:
        Balthazar.speak("Good Afternoon!", 0)
    else:
        Balthazar.speak("Good Evening!", 0)

Balthazar = Balthazar_Class()

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
with open("Languages/en.json", "w") as write_file:
    json.dump(data, write_file)
json_string = json.dumps(data)

def EnglishFunction(Balthazar, text, languages):
    website_text(Balthazar, text, languages)

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
        Balthazar.speak("My name is Greg", languages)

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

def FrenchFunction(Balthazar, text, languages):
    website_text(Balthazar, text, languages)

    if "bonjour" in text:
        Balthazar.speak("bonjour, comment allez vous?", languages)

    elif "au revoir" in text:
        Balthazar.speak("Au revoir Maître", languages)
        return 84

    if "qui est tu" in text:
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

if __name__ == "__main__":
    Welcome(Balthazar)
    languages = 0
    
    while True:
        text = Balthazar.get_audio()

        if (languages == 0):
            languages = EnglishFunction(Balthazar, text, languages)
        elif (languages == 1):
            languages = FrenchFunction(Balthazar, text, languages)
        else:
            Balthazar.speak("Error 84", 0)
            break