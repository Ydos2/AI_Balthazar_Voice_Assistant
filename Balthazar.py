import os
import time
import datetime
import json
from src.French import FrenchFunction
from src.English import EnglishFunction
from src.Class_Bathazar import Balthazar_Class

languages = 0
name = "Mathias Ressort"
age = 20

def Welcome(Balthazar):
    hour = int(datetime.datetime.now().hour)
    if (languages == 0):
        if hour >= 0 and hour < 12:
            Balthazar.speak("Good Morning!", 0)
        elif hour >= 12 and hour < 18:
            Balthazar.speak("Good Afternoon!", 0)
        else:
            Balthazar.speak("Good Evening!", 0)
    elif (languages == 1):
        if hour >= 0 and hour < 18:
            Balthazar.speak("Bonjour!", 1)
        else:
            Balthazar.speak("Bon soir!", 1)

with open('config.json') as json_file:
    data = json.load(json_file)
    languages = data['languages']
    for p in data['personalInformation']:
        name = p['name']
        age = p['age']

print(languages)
print(name)
print(age)

Balthazar = Balthazar_Class()

if __name__ == "__main__":
    Welcome(Balthazar)
    
    while True:
        text = Balthazar.get_audio(languages)

        if (languages == 0):
            languages = EnglishFunction(Balthazar, text, languages)
        elif (languages == 1):
            languages = FrenchFunction(Balthazar, text, languages)
        else:
            Balthazar.speak("Error 84", 0)
            break

        if (languages == 84):
            break