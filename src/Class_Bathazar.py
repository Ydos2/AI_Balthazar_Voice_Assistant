import os
import playsound
import speech_recognition as sr
from gtts import gTTS

class Balthazar_Class:

    def speak(self, text, lang):
        if (lang == 1):
            tts = gTTS(text=text, lang="fr")
        else:
            tts = gTTS(text=text, lang="en")
        filename = "voice.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

    def get_audio(self):
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