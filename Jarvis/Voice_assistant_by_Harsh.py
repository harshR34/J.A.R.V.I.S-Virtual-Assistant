import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import wikipedia as googleScrap
import pygame
import requests
import openai
import pyautogui
import random
from pynput.keyboard import Key,Controller
import wolframalpha
import speedtest
from time import sleep
import os
from translate import Translator
import time
import sendEmail
from sendEmail import *
import phonenumbers
from phonenumbers import geocoder
import opencage
import folium
import tkinter as tk
from tkinter import messagebox


engine = pyttsx3.init('sapi5') #'sapi5' refers to the Speech API version 5, which is a Windows-based speech synthesis API developed by Microsoft. It provides functionalities for speech synthesis and recognition on Windows platforms.
voices = engine.getProperty('voices')# the program can obtain a list of available voices.
# print(voices)

engine.setProperty('voice', voices[1].id)

def speak(audio):
    '''
    Here, say(string) method convert a string into audible speech
    and runAndWait()  method is typically used in conjunction with a text-to-speech (TTS) engine to ensure that the spoken
    audio is produced synchronously and that the program execution waits until the speech is completed before continuing.

    :param audio: Is a parameter of speech that you want to speak
    :return: an audible speach
    '''
    engine.say(audio)
    engine.runAndWait()


# wish me Function
def wishMe():
    hour = int(datetime.datetime.now().hour) # datetime is a class of datetime.py file and now() is method of datetime class
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you ?")


# Take command from user
def takeCommand():
    # It takes microphone input from the user and returns string output
    '''
    Microphone() method use to take voice input of user.This class allows Python programs to capture audio input from the microphone in real-time,
    enabling speech recognition tasks that involve listening to spoken language.

    listen(source) This method is used to capture audio input from a specified source.


    :return: string
    '''

    r = sr.Recognizer() # This is a method of Recognizer class with speech_recognition library which convert audio in text
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # The recognizer will wait for up to 1 second of silence to occur during speech input before considering the input as complete.
        audio = r.listen(source)

    try:
        #The recognize_google(audio, lang) function in the speech_recognition library is used to perform speech recognition on
        # the provided audio data using the Google Web Speech API. This function transcribes the speech contained in the audio data into text.
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Say that again please...")
        print("Say that again please...")
        return "None"
    return query

LANGUAGES = {'af': 'afrikaans',
             'sq': 'albanian',
             'am': 'amharic',
             'ar': 'arabic',
             'hy': 'armenian',
             'az': 'azerbaijani',
             'eu': 'basque',
             'bn': 'bengali',
             'bs': 'bosnian',
             'bg': 'bulgarian',
             'ca': 'catalan',
             'ceb': 'cebuano',
             'co': 'corsican',
             'hr': 'croatian',
             'cs': 'czech',
             'da': 'danish',
             'nl': 'dutch',
             'en': 'english',
             'eo': 'esperanto',
             'et': 'estonian',
             'tl': 'filipino',
             'fi': 'finnish',
             'fr': 'french',
             'gl': 'galician',
             'ka': 'georgian',
             'de': 'german',
             'el': 'greek',
             'haw': 'hawaiian',
             'iw': 'hebrew',
             'he': 'hebrew',
             'hi': 'hindi',
             'hmn': 'hmong',
             'hu': 'hungarian',
             'is': 'icelandic',
             'ig': 'igbo',
             'id': 'indonesian',
             'it': 'italian',
             'ja': 'japanese',
             'kn': 'kannada',
             'kk': 'kazakh',
             'km': 'khmer',
             'ko': 'korean',
             'ky': 'kyrgyz',
             'lo': 'lao',
             'la': 'latin',
             'lv': 'latvian',
             'lt': 'lithuanian',
             'lb': 'luxembourgish',
             'mk': 'macedonian',
             'mg': 'malagasy',
             'ms': 'malay',
             'ml': 'malayalam',
             'mt': 'maltese',
             'mi': 'maori',
             'mr': 'marathi',
             'mn': 'mongolian',
             'ne': 'nepali',
             'no': 'norwegian',
             'ps': 'pashto',
             'fa': 'persian',
             'pl': 'polish',
             'pt': 'portuguese',
             'ro': 'romanian',
             'ru': 'russian',
             'sm': 'samoan',
             'gd': 'scots gaelic',
             'sr': 'serbian',
             'sn': 'shona',
             'sd': 'sindhi',
             'si': 'sinhala',
             'sk': 'slovak',
             'sl': 'slovenian',
             'so': 'somali',
             'es': 'spanish',
             'su': 'sundanese',
             'sw': 'swahili',
             'sv': 'swedish',
             'tg': 'tajik',
             'ta': 'tamil',
             'te': 'telugu',
             'th': 'thai',
             'tr': 'turkish',
             'uk': 'ukrainian',
             'uz': 'uzbek',
             'vi': 'vietnamese',
             'cy': 'welsh',
             'xh': 'xhosa',
             'yi': 'yiddish',
             'yo': 'yoruba',
             'zu': 'zulu'}

def translateLang(text,lang_code):
    '''
    Translator is class that is contain to_lang var that is contain a lang_code in which text want to translate.

    translate(text) which convert user text in lang_code language

    :param text: Text that you want to translate
    :param lang_code: language code in which text want to translate
    :return: translated text
    '''
    translators = Translator(to_lang=LANGUAGES[lang_code])
    translated_text = translators.translate(text)
    print(f"{LANGUAGES[lang_code]} : {translated_text}")
    speak(f"In {LANGUAGES[lang_code]} the text - '{text}' is '{translated_text}'")

def get_weather(city):
    '''
    get(url) which is commonly used for making HTTP requests.
    Specifically, requests.get() is used to send an HTTP GET request to the specified URL and retrieve the response from the server.

    The json() method in Python is typically used to decode a JSON formatted string into a Python data structure, usually a dictionary

    :param city: which define a city for which you want to find weather of it
    :return: all details of weather about searched city
    '''
    api_key = 'YOUR_API_KEY' #create a account in Open Weather map API
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(base_url)
    data = response.json()

    if data['cod'] == '404':
        speak('City not found. Please try again.')
        return

    weather_desc = data['weather'][0]['description']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(f"Weather desc : {weather_desc}")
    print(f"Temp : {temp}\u00B0")
    print(f"Humidity : {humidity} %")
    print(f"Wind_speed : {wind_speed}mph")

    speak(
        f'The weather in {city} is {weather_desc}. The temperature is {temp} degrees Celsius, humidity is {humidity}%, and wind speed is {wind_speed} miles per hour.')


# Add this function call inside your while loop where you handle commands

# Take command for play offline song
def takeCommandForSongs():
    # It takes microphone input from the user and returns string output
    '''
    Modified method for take Command for songs
    :return: Query convert from audio into text
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tell Which song do you what to play...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def track_phone():
    number = phone_entry.get()
    root.destroy()
    if not number:
        print("Error", "Please enter a phone number")
    else:
        pepnumber = phonenumbers.parse(number)
        print(pepnumber)
        location = phonenumbers.geocoder.description_for_number(pepnumber, "en")
        print(location)

        from phonenumbers import carrier
        service_provider = phonenumbers.parse(number)
        print(carrier.name_for_number(service_provider, "en"))

        from opencage.geocoder import OpenCageGeocode

        key = "YOUR_API_KEY" #create a account in OpenCageGeocoder API
        geocoder = OpenCageGeocode(key)
        qurey = str(location)
        result = geocoder.geocode(qurey)

        print(result)
        lng = result[0]['geometry']['lng']
        lat = result[0]['geometry']['lat']

        myMap = folium.Map(location=[lat, lng], zoom_start=9)
        folium.Marker([lat, lng], popup=location).add_to(myMap)

        myMap.save(f"{location}_location.html")

# search on google
def searchGoogle(query):
    '''
    webbrowser is module for websearch
    open() is a method that is open any query in google by give google URL.
    :param query: for search in google
    :return:
    '''
    if "google" in query:
        if "elephant" in query :
            print("That is restricted data from google you can't search.")
            speak("That is restricted data from google you can't search.")
        else :
            query = query.replace("jarvis", "")
            query = query.replace("google search", "")
            query = query.replace("google", "")
            speak("This is what I found on google")

            try:
                webbrowser.open(f"https://www.google.com/search?q={query}")
                result = googleScrap.summary(query, 1)
                speak(result)

            except:
                print()
    #
#
# search on youtube
def searchYoutube(query):
    '''
    webbrowser is module for websearch
    :param query: for search in youtube
    :return:
    '''
    if "youtube" in query:
        if "elephant" in query :
            print("That is restricted data from youtube you can't search.")
            speak("That is restricted data from youtube you can't search.")
        else :
            speak("This is what I found for your search!")
            query = query.replace("youtube search", "")
            query = query.replace("youtube", "")
            query = query.replace("jarvis", "")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            speak("Done, Sir")


# search on wikipedia
def searchWikipedia(query):
    '''

    wikipedia.summary() is a function typically used in Python programming language when working with the Wikipedia API.
    This function retrieves a summary of the requested Wikipedia page.
    It takes a single argument, which is the title of the page or a search query.

    :param query: for search in wikipedia
    :return:
    '''
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia", "")
        query = query.replace("search wikipedia", "")
        query = query.replace("jarvis", "")
        results = wikipedia.summary(query, sentences=10)
        speak("According to wikipedia..")
        print(results)
        speak(results)


dictapp = {"commandprompt": "cmd", "paint": "paint", "word": "winword", "excel": "excel", "chrome": "chrome",
           "vs code": "code", "powerpoint": "powerpnt","clock" : "clock"}


def openappweb(query):

    '''
    system() method is a function in Python's os module used to execute operating system commands.

    :param query: to any app you want or website
    :return:
    '''
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")


def closeappweb(query):
    speak("Closing,sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")

    elif "4 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")

#Alarm


def set_alarm(hour, minute, music_file):
    '''
    1. pygame.init(): This method initializes all imported pygame modules.
    It must be called before any other pygame functions are used.

    2. pygame.mixer.init(): This method initializes the mixer module.
     It must be called before using any of the mixer functions.
     The mixer module allows you to control playback of sound samples and music.

    3. time.localtime(): This method in the time module returns the current time as a named
     tuple containing attributes like year, month, day, hour, minute, etc., according to the
      local time zone.

    4. pygame.mixer.music.load(music_file): This method loads a music file for playback.
     The music_file parameter should be the path to the music file you want to load.

    5.pygame.mixer.music.play(): This method starts playback of the currently loaded music file.

    6.pygame.mixer.music.get_busy(): This method returns True if the music playback is
     currently active, meaning that the music is still playing.

    7. pygame.time.Clock().tick(10): This method sets the maximum frame rate.
      It limits the frame rate to a specified value (in this case, 10 frames per second).
      This function is typically used in games to control the frame rate, but in this context,
       it's being used to wait for the music to finish playing before breaking out of the loop.

    8. time.sleep(60): This method in the time module pauses the execution of the script for the specified number of
        seconds (in this case, 60 seconds or 1 minute). It's used here to check the current time every minute and see if
        it matches the specified alarm time.

    :param hour: alarm hours
    :param minute: alarm minutes
    :param music_file: music that want to play as an alarm music
    :return:
    '''
    pygame.init()
    pygame.mixer.init()

    while True:
        current_time = time.localtime()
        if current_time.tm_hour == hour and current_time.tm_min == minute:
            print("Time's up! Alarm ringing...")
            # Load and play the music file
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            break
        time.sleep(60)  # Check every minute

keyboard = Controller()

def volumeup():
    '''

    keyboard.press(Key.media_volume_up): This method is used to simulate a key press event for the media volume up key.
    It's part of the keyboard module, and Key.media_volume_up is a constant representing the media volume up key.

    keyboard.release(Key.media_volume_up): This method is used to simulate a key release event for the media volume up key.
     It's also part of the keyboard module.

    :return:
    '''
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
def volumedown():
    '''

    keyboard.press(Key.media_volume_up): This method is used to simulate a key press event for the media volume up key.
    It's part of the keyboard module, and Key.media_volume_down is a constant representing the media volume down key.

    keyboard.release(Key.media_volume_up): This method is used to simulate a key release event for the media volume up key.
     It's also part of the keyboard module.

    :return:
    '''
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)

def WolfRamAlpha(query):
    '''
        wolframalpha.Client(apikey) :-  That is a method for communicating with the Wolfram Alpha API.
        It uses the API key defined earlier to authenticate the client.

        requester.query(query) :- This method sends a query to the Wolfram Alpha API using the client object created earlier.
         The query is the user-provided input for mathematical calculation.

        :param query: input from user for calculate any mathematical calculation
        :return: answer of calculation
    '''
    apikey = "YOUR_API_KEY" #CREATE AN ACCOUNT IN WOLF_RAM_ALPHA AND GET YOUR OWN API
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def stop_song():
    """Stop the currently playing song. when you play song from internal folder not from any music app like spotify or Gaana."""
    speak("Song stop successfully")
    pygame.mixer.init()  # Initialize the mixer module
    pygame.mixer.music.stop()  # Stop the currently playing music
def Calc(query):
    '''
        This method use WolfRamAlpha method for do all mathematical calculation
        It takes a query of calculation from user and give result of this query

        :param query: for mathematical calculation
        :return:
    '''
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"result :- {result}")
        speak(f"{Final} is equal to {result}")

    except:
        speak("The value is not answerable")


def game_play():
    speak("Lets Play ROCK PAPER SCISSORS !!")
    print("LETS PLAYYYYYYYYYYYYYY")
    i = 0
    Me_score = 0
    Com_score = 0
    while (i < 5):
        choose = ("rock", "paper", "scissors")  # Tuple
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if (query == "rock"):
            if (com_choose == "rock"):
                speak("ROCK")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "paper"):
            if (com_choose == "rock"):
                speak("ROCK")
                Me_score += 1
                print(f"Score:- ME :- {Me_score + 1} : COM :- {Com_score}")

            elif (com_choose == "paper"):
                speak("paper")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                speak("ROCK")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
        i += 1

    print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "hello" in query:
            speak("Hello sir, how are you ?")
        elif "i am fine" in query:
            speak("that's great, sir")
        elif "how are you" in query:
            speak("Perfect, sir")
        elif "thank you" in query:
            speak("you are welcome, sir")
        elif "finally sleep" in query:
            speak("Going to sleep,sir")
            exit()

        elif 'the time' in query:
            '''
            .strftime("%H:%M:%S"): This method is called on the datetime object to format the date and time as a string. 
            '''
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'track phone number' in query :
            speak("Ok Boss !")
            speak("Please enter phone number in given dialog box named Track !")
            root = tk.Tk()
            root.title("Phone Number Tracker")

            phone_label = tk.Label(root, text="Enter Phone Number:")
            phone_label.pack()

            phone_entry = tk.Entry(root)
            phone_entry.pack()
            track_button = tk.Button(root, text="Track", command=track_phone)
            track_button.pack()
            root.mainloop()

        elif "google" in query:
            searchGoogle(query)

        elif "youtube" in query:
            searchYoutube(query)

        elif "wikipedia" in query:
            searchWikipedia(query)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        # elif "open" in query:
        #     openappweb(query)
        elif "close" in query:
            closeappweb(query)

        elif "set an alarm" in query:
            speak("Ok Boss !")
            speak("Enter hour of timer")
            hr = int(input("Enter hour of timer : "))
            speak("Enter minutes of timer")
            min = int(input("Enter minutes of timer : "))

            set_alarm(hr,min,"D:\\Songs\\stranger_things.mp3")
            continue

        elif "pause video" in query:
            pyautogui.press("k")
            speak("video paused")
        elif "play video" in query:
            pyautogui.press("k")
            speak("video played")
        elif "mute video" in query:
            pyautogui.press("m")
            speak("video muted")

        elif "volume up" in query:
            speak("Turning volume up,sir")
            volumeup()
        elif "volume down" in query:
            speak("Turning volume down, sir")
            volumedown()

        elif "remember that" in query:
            speak("Ok Boss !")
            rememberMessage = query.replace("remember that", "")
            rememberMessage = query.replace("jarvis", "")
            speak("You told me to remember that" + rememberMessage)
            remember = open("Remember.txt", "a")
            remember.write(rememberMessage)
            remember.close()
        elif "what do you remember" in query:
            speak("Ok Boss !")
            remember = open("Remember.txt", "r")
            speak("You told me to remember that" + remember.read())

        elif "tired" in query:
            speak("Playing your favourite songs, sir")
            a = (1, 2, 3)
            b = random.choice(a)
            if b == 1:
                webbrowser.open("https://youtu.be/QXJyMpxd210?si=oSnZ4rJwKvDJ4pmKk")
            if b == 2:
                webbrowser.open("https://www.youtube.com/watch?v=2Vv-BfVoq4g")
            if b == 3:
                webbrowser.open("https://www.youtube.com/watch?v=Rif-RTvmmss")


        elif "calculate" in query:
            speak("Ok Boss !")
            query = query.replace("calculate", "")
            query = query.replace("jarvis", "")
            Calc(query)

        elif "play a game" in query:
            game_play()

        elif "screenshot" in query:
            speak("Ok Boss !")
            im = pyautogui.screenshot()
            file_path = "D:/SEM_3_PROJECTS/Individual project/JarvisAI/screenshot.png"
            im.save(file_path)
            speak("screenshot is taken successfully")

        elif "schedule my day" in query:
            speak("Ok Boss !")
            tasks = []  # Empty list
            speak("Do you want to clear old tasks (Plz speak YES or NO)")
            query = takeCommand().lower()
            if "yes" in query:
                file = open("tasks.txt", "w")
                file.write(f"")
                file.close()
                no_tasks = int(input("Enter the no. of tasks :- "))
                i = 0
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt", "a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()
            elif "no" in query:
                i = 0
                no_tasks = int(input("Enter the no. of tasks :- "))
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt", "a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()

        elif "internet speed" in query:
            speak("Ok Boss, I search it from my resources .")
            wifi = speedtest.Speedtest()
            upload_net = wifi.upload() / 1048576  # Megabyte = 1024*1024 Bytes
            download_net = wifi.download() / 1048576
            print("Wifi download speed is ", download_net)
            speak(f"Wifi download speed is {download_net}")
            print("Wifi Upload Speed is", upload_net)
            speak(f"Wifi Upload speed is {upload_net}")

        elif "ipl score" in query:
            '''        
                plyer.notification: This module provides a cross-platform API for displaying notifications. In the code snippet, it is used to display a notification with IPL match scores.

                bs4.BeautifulSoup: This module is part of the BeautifulSoup library, which is a popular Python library for web scraping. BeautifulSoup is used to parse HTML and XML documents. In the code snippet, it is used to parse the HTML content of a webpage fetched using urllib.request.
                
                web sracping : Web scraping is the process of automatically extracting data from websites. It involves fetching the HTML code of a web page and then parsing it to extract the desired information. This information can include text, images, links, structured data, and more.
                
                urllib.request: This module allows you to open URLs. In the code snippet, it is used to open a URL (https://www.cricbuzz.com/) to fetch the webpage content.
                
                notification.notify : This method is provided by the plyer.notification module. It is used to display a notification with the specified title, message, and timeout duration.
                
                Now, let's explain the methods used in the code snippet:
                
                urllib.request.urlopen(url): This method opens the URL specified by the url variable and returns a response object.
                
                BeautifulSoup(page, "html.parser"): This creates a BeautifulSoup object soup by parsing the HTML content of the webpage fetched using urllib.request.urlopen(url).
                
                find_all(class_="cb-ovr-flo cb-hmscg-tm-nm"): This method finds all HTML elements with the specified CSS class (cb-ovr-flo cb-hmscg-tm-nm). It returns a list of matching elements.
                
                get_text(): This method retrieves the text content of an HTML element.
                
                notification.notify(...): This method displays a notification with the specified title, message, and timeout duration using the plyer.notification module.
            '''
            from plyer import notification
            from bs4 import BeautifulSoup
            import urllib.request

            url = "https://www.cricbuzz.com/"
            page = urllib.request.urlopen(url)
            soup = BeautifulSoup(page, "html.parser")

            # Find team names
            team_elements = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")
            if len(team_elements) >= 2:
                team1 = team_elements[0].get_text()
                team2 = team_elements[1].get_text()
            else:
                team1 = "Team 1"
                team2 = "Team 2"

            # Find team scores
            score_elements = soup.find_all(class_="cb-ovr-flo")
            if len(score_elements) >= 11:  # Assuming scores are at these positions
                team1_score = score_elements[8].get_text()
                team2_score = score_elements[10].get_text()
            else:
                print("Error: Could not find team scores.")
                team1_score = "N/A"
                team2_score = "N/A"

            print(f"{team1} : {team1_score}")
            print(f"{team2} : {team2_score}")
            ipl_teams = [
                "Chennai Super Kings",
                "Delhi Capitals",
                "Punjab Kings",
                "Kolkata Knight Riders",
                "Mumbai Indians",
                "Rajasthan Royals",
                "Royal Challengers Bangalore",
                "Sunrisers Hyderabad",
                "Gujarat Titans",
                "Lucknow Super Giants"
            ]
            if team1_score in ipl_teams:
                speak("The match has not started yet but it will start in the evening.")
                speak("Thanks for use me for IPL information.")

            notification.notify(
                title="IPL SCORE :- ",
                message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
                timeout=15
            )

        elif "translate" in query:

            speak("Say anything that you want to translate")
            print("Say anything that you want to translate")
            text = takeCommand().lower()
            speak("In which language you want to translate your text ?")
            print(LANGUAGES)
            lang_code = input("Enter language code in which you want to translate the text : ")
            translateLang(text,lang_code)



        elif "open" in query:  # EASY METHOD
            query = query.replace("open", "")
            query = query.replace("jarvis", "")
            pyautogui.press("super") # Windows key is also known as super key
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        elif 'open spotify.com' in query:
            webbrowser.open("spotify.com")

        elif 'play song' in query:
            speak("Sure , which song do you want to play offline ?")
            content = takeCommandForSongs().capitalize()
            song_dir = "D:\\Songs\\"
            songsList = os.listdir(song_dir)
            # print(content)
            if content + ".mp3" in songsList:
                pygame.init()
                pygame.mixer.music.load(song_dir + content + '.mp3')
                pygame.mixer.music.play()

        elif 'stop song' in query:
            stop_song()

        elif 'send email' in query:
                to = input("Enter Receiver's Email id : ")
                speak("What should I say in Subject ?")
                subject = takeCommand()
                speak("What should I say in Content ?")
                content = takeCommand()
                sendEmail.send_email(to,subject, content)
                speak("Email has been sent!")

        elif "weather" in query:
            speak('Please tell me the city name.')
            city = takeCommand()
            get_weather(city)



        elif 'search on youtube' in query:
            speak("Sure, what do want to search ?")
            content = takeCommand()
            webbrowser.open(f"https://www.youtube.com/results?search_query={content}")
            speak(f"Playing {content} from YouTube")

        elif 'can you please terminate' in query:
            speak("Ok boss, Thanks for use me !")
            break;


'''

VOICE ASSISTANT DOCS    
It seems like you've provided a comprehensive Python script implementing a voice-controlled assistant similar to Jarvis. This script incorporates various functionalities such as:

Voice recognition and speech synthesis using speech_recognition and pyttsx3.
Retrieving information from Wikipedia, Google, and YouTube.
Opening applications and websites.
Setting alarms and reminders.
Controlling system volume.
Playing games like Rock Paper Scissors.
Taking screenshots.
Translating text into different languages.
Getting weather updates.
Calculating internet speed.
Translating text.
Opening files and applications using PyAutoGUI.
Overall, this script provides a wide range of functionalities for interacting with the computer through voice commands. If you have any specific questions or need assistance with any part of the script, feel free to ask!
'''