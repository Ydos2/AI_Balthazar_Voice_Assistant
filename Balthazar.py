import os
import time
import datetime
import json
from src.French import FrenchFunction
from src.English import EnglishFunction
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

if __name__ == "__main__":
    Welcome(Balthazar)
    languages = 0
    
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