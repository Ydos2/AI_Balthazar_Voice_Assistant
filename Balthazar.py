import os
import time
import datetime
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
if __name__ == "__main__":
    Welcome(Balthazar)
    languages = 0
    while True:
        text = Balthazar.get_audio()
        
        website_text(Balthazar, text, languages)

        if "hello" in text:
            Balthazar.speak("hello, how are you?", languages)

        elif "goodbye" in text:
            Balthazar.speak("Goodbye Master", languages)
            break

        elif "language" in text:
            if "French" in text:
                languages = 1
                Balthazar.speak("J'ai changer le language en Français", languages)
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