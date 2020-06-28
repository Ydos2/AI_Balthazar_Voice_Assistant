import os
import time
import datetime
from src.website import website_text
from src.Class_Bathazar import Balthazar_Class

def Welcome(Balthazar):
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        Balthazar.speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        Balthazar.speak("Good Afternoon!")
    else:
        Balthazar.speak("Good Evening!")

Balthazar = Balthazar_Class()
if __name__ == "__main__":
    Welcome(Balthazar)
    while True:
        text = Balthazar.get_audio()
        
        website_text(Balthazar, text)

        if "hello" in text:
            Balthazar.speak("hello, how are you?")

        elif "goodbye" in text:
            Balthazar.speak("Goodbye Master")
            break

        elif "what is your name" in text:
            Balthazar.speak("My name is Greg")

        elif 'play music' in text:
            music_dir = './'  #Your Path
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            Balthazar.speak(f"Sir, the time is {strTime}")

        else:
            Balthazar.speak("Sorry, i don't understand my master")