import webbrowser
import wikipedia
import re
import platform
import os

def website_text(Balthazar, text, languages):
    if "Wikipedia" in text:
        Balthazar.speak('Searching Wikipedia...', languages)
        text = text.replace("wikipedia", "")
        results = wikipedia.summary(text, sentences=2)
        Balthazar.speak("According to Wikipedia", languages)
        print(results)
        Balthazar.speak(results)

    elif 'open YouTube' in text:
        webbrowser.open("youtube.com", 2)

    elif 'open Google' in text:
        webbrowser.open("google.com", 2)

    elif 'open stackoverflow' in text:
        webbrowser.open("stackoverflow.com", 2)

    elif 'open Reddit' in text:
        reg_ex = re.search('open reddit (.*)', text)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url, 2)

    elif 'open website' in text:
        reg_ex = re.search('open website (.+)', text)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url, 2)
            print('Done!')
        else:
            pass

    elif 'close chrome' in text:
        Balthazar.speak("Chrome is close.", languages)
        system_txt = platform.system()
        if (system_txt == 'Linux'):
            browserExe = "chrome"
            os.system("pkill " + browserExe)
        else:
            browserExe = "chrome.exe"
            os.system("taskkill /f /im " + browserExe)

    elif 'close Firefox' in text:
        Balthazar.speak("Firefox is close.", languages)
        system_txt = platform.system()
        if (system_txt == 'Linux'):
            browserExe = "firefox"
            os.system("pkill " + browserExe)
        else:
            browserExe = "firefox.exe"
            os.system("taskkill /f /im " + browserExe)