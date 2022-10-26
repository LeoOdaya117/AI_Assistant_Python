import pyautogui
import datetime
import time
import pyttsx3 as py
import pywhatkit
import speech_recognition as sr
import webbrowser
import subprocess
import os
import wikipedia

time.sleep(1)
r = sr.Recognizer()
engine = py.init()
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine.say("Hi master Leo, what can i do for you today?")
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def to_do(text):
    if 'open' in text:
        text = text.replace('open', '')

        if '.com' in text or 'dotcom' in text or 'classroom' in text:
            text = text.replace('dotcom', '.com')
            text = text.replace(' ', '')
            new = 2
            url = text
            if 'classroom' in text:
                talk("Opening google " + text)
                url = 'classroom.google.com'
            else:
                talk("Opening " + text)
            chrome_path = "C:/Users/Leo/AppData/Local/Programs/Opera/launcher %s"
            webbrowser.get(chrome_path).open(url, new=new)
        elif 'notepad' in text:
            talk("Opening " + text)
            p = subprocess.Popen("notepad")
        elif 'control panel' in text:
            talk("Opening " + text)
            p = subprocess.Popen("cmd /c control")
        elif 'firefox' in text:
            talk("Opening " + text)
            p = subprocess.Popen("C:/Program Files/Mozilla Firefox/firefox.exe")
        elif 'vs code' in text:
            talk("Opening " + text)
            p = subprocess.Popen("C:/Users/Leo/AppData/Local/Programs/Microsoft VS Code/Code")
        elif 'calculator' in text:
            talk("Opening " + text)
            p = subprocess.Popen("Calculator.exe")
        elif 'opera' in text:
            talk("Opening " + text)
            p = subprocess.Popen("C:/Users/Leo/AppData/Local/Programs/Opera/launcher")
        elif 'microsoft word' in text:
            talk("Opening " + text)
            p = subprocess.Popen("C:/Program Files/Microsoft Office/root/Office16/WINWORD")
        elif 'powerpoint' in text:
            talk("Opening " + text)
            p = subprocess.Popen("C:/Program Files/Microsoft Office/root/Office16/POWERPNT")
        elif 'telegram' in text:
            talk("Opening " + text)
            p = subprocess.Popen("C:/Users/Leo/AppData/Roaming/Telegram Desktop/telegram")
        elif 'excel' in text:
            talk("Opening " + text)
            p = subprocess.Popen("C:/Program Files/Microsoft Office/root/Office16/EXCEL")
        elif 'access' in text:
            talk("Opening " + text)
            p = subprocess.Popen("C:/Program Files/Microsoft Office/root/Office16/MSACCESS")
        elif 'visual studio' in text:
            talk("Opening " + text)
            p = subprocess.Popen("C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/Common7/IDE/devenv")
        elif 'jcreator' in text:
            talk("Opening " + text)
            p = subprocess.Popen("C:/Program Files (x86)/Xinox Software/JCreatorV4/JCreator")
        elif 'baloran' in text:
            talk("Opening " + text)
            p = subprocess.Popen("C:/Riot Games/Riot Client/RiotClientServices.exe")
        elif 'capcut' in text:
            talk("Opening " + text)
            p = subprocess.Popen("C:/Users/Leo/AppData/Local/CapCut/Apps/CapCut.exe")
        elif 'shareit' in text:
            talk("Opening " + text)
            p = subprocess.Popen("SHAREit-KCWEB.exe")
        elif 'github' in text:
            talk("Opening " + text)
            p = subprocess.Popen("C:/Users/Leo/AppData/Local/GitHubDesktop/GitHubDesktop")
        elif 'sublime' in text:
            talk("Opening " + text)
            p = subprocess.Popen("C:/Program Files/Sublime Text 3/sublime_text.exe")
        else:
            talk("Master i can't understand!")

    elif 'play' in text:
        text = text.replace('play', '')
        talk("Playing " + text)
        pywhatkit.playonyt(text)
    elif 'good job' in text:
        talk("Thank you Master Leo")
    elif 'pause' in text:
        pyautogui.hotkey(' ')
    elif 'resume' in text:
        pyautogui.hotkey(' ')
    elif 'close' in text:
        close_prog(text)
    elif 'search for' in text or 'search' in text or 'what is' in text:
        text = text.replace('search', '')
        text = text.replace('for', '')
        text = text.replace('what is', '')
        text = text.replace('what is the', '')

        if 'current time' in text:
            now = datetime.datetime.now()
            talk("Current time is " + now.strftime("%c"))
            print("now =", now.strftime("%c"))
        else:
            talk("Searching for " + text)
            result = wikipedia.search(text)
            page = wikipedia.page(result)
            page.title
            page.url
            page.content
            print(wikipedia.page(page).summary)
            talk("According to wikipedia, " + wikipedia.page(page).summary)
    elif 'shutdown' in text:
        talk("Shutting Down")
        pyautogui.hotkey('winleft', 'd')
        pyautogui.hotkey('alt', 'f4')
        pyautogui.press('enter')
    elif 'restart' in text:
        talk("Restarting")
        pyautogui.hotkey('winleft', 'd')
        pyautogui.hotkey('alt', 'f4')
        pyautogui.press('down', 'enter')
    elif 'sleep' in text:
        talk("Restarting")
        pyautogui.hotkey('winleft', 'd')
        pyautogui.hotkey('alt', 'f4')
        pyautogui.press('down', 'down', 'enter')
    else:
        talk("Master i can't understand!")


def close_prog(text):
    text = text.replace('close', '')
    talk("Closing " + text)
    if 'current tab' in text:
        pyautogui.hotkey('ctrl', 'w')
    elif 'chrome' in text:
        os.system('TASKKILL /F /IM chrome.exe')
    elif 'notepad' in text:
        os.system('TASKKILL /F /IM notepad.exe')
    elif 'microsoft word' in text:
        os.system('TASKKILL /F /IM WINWORD.exe')
    elif 'powerpoint' in text:
        os.system('TASKKILL /F /IM POWERPNT.exe')
    elif 'telegram' in text:
        os.system('TASKKILL /F /IM telegram.exe')
    elif 'excel' in text:
        os.system('TASKKILL /F /IM EXCEL.exe')
    elif 'access' in text:
        os.system('TASKKILL /F /IM MSACCESS.exe')
    elif 'vs code' in text:
        os.system('TASKKILL /F /IM Code.exe')
    elif 'calculator' in text:
        os.system('TASKKILL /F /IM Calculator.exe')
    elif 'visual studio' in text:
        os.system('TASKKILL /F /IM devenv.exe')
    elif 'jcreator' in text:
        os.system('TASKKILL /F /IM JCreator.exe')
    elif 'baloran' in text:
        os.system('TASKKILL /F /IM RiotClientServices.exe')
    elif 'baloran' in text:
        os.system('TASKKILL /F /IM CapCut.exe')
    elif 'shareit' in text:
        os.system('TASKKILL /F /IM SHAREit-KCWEB.exe')
    elif 'github' in text:
        os.system('TASKKILL /F /IM GitHubDesktop.exe')
    elif 'firefox' in text:
        os.system('TASKKILL /F /IM firefox.exe')
    elif 'sublime' in text:
        os.system('TASKKILL /F /IM sublime_text.exe')

while True:

    with sr.Microphone() as inp:
        try:
            os.system('cls')
            print("\nListening.......")
            r.adjust_for_ambient_noise(inp, 0.2)
            audio = r.listen(inp)
            text = r.recognize_google(audio)
            text = text.lower()

            if 'jarvis' in text:
                text = text.replace('jarvis','')
                print(text)
                to_do(text)

        except:
            print("\nCould not understand")
            r = sr.Recognizer()
            continue


