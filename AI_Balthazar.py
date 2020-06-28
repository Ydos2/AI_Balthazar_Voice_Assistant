import os
import time
import datetime
import playsound
import webbrowser
import wikipedia
import speech_recognition as sr
import re
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

Open = True
if __name__ == "__main__":
    wishMe()
    while Open:
        text = get_audio()

        if "hello" in text:
            speak("hello, how are you?")
        
        elif "goodbye" in text:
            speak("Goodbye Master")
            Open = False

        elif "what is your name" in text:
            speak("My name is Greg")

        elif "Wikipedia" in text:
            speak('Searching Wikipedia...')
            text = text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open YouTube' in text:
            webbrowser.open("youtube.com")

        elif 'open Google' in text:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in text:
            webbrowser.open("stackoverflow.com")
   
        elif 'open Reddit' in text:
            reg_ex = re.search('open reddit (.*)', text)
            url = 'https://www.reddit.com/'
            if reg_ex:
                subreddit = reg_ex.group(1)
                url = url + 'r/' + subreddit
            webbrowser.open(url)

        elif 'open website' in text:
            reg_ex = re.search('open website (.+)', text)
            if reg_ex:
                domain = reg_ex.group(1)
                url = 'https://www.' + domain
                webbrowser.open(url)
                print('Done!')
            else:
                pass

        elif 'play music' in text:
            music_dir = 'D:./'  #Your Path
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        else:
            speak("Sorry, i don't understand my master")