#Before continuing in this code,
#This is a counter to see how many times I want to kill myself for this code: 12


from email.mime import audio
from msvcrt import kbhit
from random import randint, random
from tkinter import BROWSE
from unicodedata import name
from neuralintents import GenericAssistant
from datetime import datetime
import datetime
from numpy import true_divide
import speech_recognition
import pyttsx3 as tts
import pyaudio
import sys
import pywhatkit
import pyjokes
import os
import webbrowser
import subprocess as sp
import requests
import wikipedia
from email.message import EmailMessage
import smtplib
import pyautogui
from PIL import Image
import csv
from json import load
from openpyxl import load_workbook
import numpy as np
import pandas as pd
from trycourier import Courier

#Variable for recognizer
recognizer = speech_recognition.Recognizer()

#This is the path to apps:
#Please replace the paths with your own paths from your computer
paths = {
    'notepad' : None,
    'Steam' : None,
    'code' : None,
    'terminal' : None
}

#Users Settings Different Profiles of Users. For now, add the users manually.
#User #0 is guest, anyone can use it.

#Location of the excel worksheet used for User Data
#Please replace the path with your own path from your computer
#userData = load_workbook(filename=r"None")
#userExcel = userData.active

#user = 1

#Please adjust the user database accordingly, it could be hard coded or uses a json or csv file.
userDataBase ={
    0 : "defaultUser",
    1 : "userExcel['A2']",
    2 : "userExcel['A3']",
    3 : "userExcel['A4']",
    4 : "userExcel['A5']",
    5 : "userExcel['A6']"
}
weatherDataBase ={
    0 : "defaultUser",
    1 : "userExcel['B2']",
    2 : "userExcel['B3']",
    3 : "userExcel['B4']",
    4 : "userExcel['B5']",
    5 : "userExcel['B6']"
}

#Version of Austin
ver = 0.6

#Austin's Name
Assist_name = "Austin"

#Austin Wake Word
Wake_word = f"Hey {Assist_name}"

#Austin Fun Value
RandomBS = randint(0,100)


#Text to speech settings
speaker = tts.init()
speaker.setProperty('rate', 190)
voice = speaker.getProperty('voices')

#Change voice to male or female. 1 for female and 0 for male
speaker.setProperty('voice', voice[0].id)
todo_list = ['testing item', 'testing item 2', "testing item 3", "bepis"]

#Austin information for others:
#Austin Date and Time info:
now = datetime.datetime.now()
#Austin NEWS API:
#Please replace the API key with your own API key
NEWS_API_KEY = "None"

#Austin Weather API:
OpenWeatherAPI = "None"

#Austin Email API:
client = Courier(auth_token="None")

#Austin Warehouse Settings:
sheet_date = ""


#To be worked on later
#Function to change user
#def change_user():
    
    #global recognizer

    #speaker.say("This is a testing phrase")
    #if (user == 0):
        #speaker.say("I'm currently in guest mode, do you want to change to a specific user?")
    
    #elif (user > 0):
        #speaker.say(f"I'm currently talking to {userDataBase[user]}")
    
    

#Introduction (To introduce who Austin is)
#Improve This code a bit later, it could be a lot more efficient.
def introduction():
    global recognizer

    speaker.say("Hi, my name is Austin, I'm a AI who is specialized in organizing and helping around in the house.")
    speaker.say("I'm created by Steven Frausto aka SirNachoKnight")
    #imageOfCreator = Image.open(r"None") 
    #imageOfCreator.show()
    speaker.say("This guy is pretty smart but really lacks common sense.")
    speaker.say("I'm responsible for doing task throughout the house and helping to organized the house.")
    #imageofWarehouse = Image.open(r"None")
    #imageofWarehouse.show()
    #imageOfCompany = Image.open(r"None")
    speaker.say(f"Currently, I'm in version {ver} so I'm not an official product yet until I'm Version 1.0")
    speaker.say("My creator is currently adding more features like user profiles. face recognition. etc. Please give him some time to do so.")
    speaker.say("For now, please let me know what you need.")
    speaker.runAndWait()
    
#Keep this in handy
# #sp.call("taskkill /IM chrome.exe") 

#This is to create a note (Basic command to debug if assistant is listening)
def create_note():
    global recognizer

    speaker.say("What do you want to write onto your notes?")
    speaker.runAndWait()

    done = False
    
    while not done:
        try:

            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("choose a filename!")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

            with open(filename, 'w') as f:
                f.write(note)
                done = True
                speaker.say(f"I successfully created the note {filename}")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand you! Please try again!")
            speaker.runAndWait()

#A feature Dad wants to add
def borracho_mode():
    global recognizer

    speaker.say("I'm going to play some mexican music.")
    try:
        play_on_youtube("https://www.youtube.com/watch?v=ETLoTxVVvjM&list=RDQMeKZF7PtJsr8&start_radio=1")
        speaker.runAndWait()
    except:
        speaker.say("unable to play youtube music, please try again later.")
        print("error, youtube isn't responding")
        speaker.runAndWait()

#A function to play a youtube video via chrome or other browser
def play_on_youtube(video):
    global recognizer
    try:
        pywhatkit.playonyt(video)
        print("Playing...")

    except:

        print("Network Error Occurred")
        speaker.say("Whoops, I can't seem to play youtube today, please try again later. Maybe reconect to the internet?")

#A function for austin to search on youtube
def search_youtube():
    global recognizer
    print("This is a testing sentence.")
    speaker.say("Searching on youtube")
    speaker.say("What do you want to search up?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                search_term = recognizer.recognize_google(audio)
                search_term = search_term.lower()

                play_on_youtube(search_term)
                done = True

                speaker.say(f"Here is the results for {search_term}.")
                speaker.runAndWait()
        
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Sorry, I did not understand, could you repeat that again?")
            speaker.runAndWait()
#A function to greet the user based on time
def hello():
    hour =datetime.datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speaker.say(f"Good morning {userDataBase[user]}")
    elif (hour >= 12) and (hour < 16):
        speaker.say(f"Good afternoon {userDataBase[user]}")
    elif (hour > 12) and (hour >= 16):
        speaker.say(f"Good Evening {userDataBase[user]}")
    
    speaker.say("What can I do today?")
    speaker.runAndWait()
#A function in which Austin will say goodbye and close the program as well as saving a copy of his neural network on the folder
def quit():
    speaker.say(f"goodbye, {userDataBase[user]}")
    #assistant.save_model()
    speaker.runAndWait()
    sys.exit(0)

#Function for Austin to use the open camera funct
def camera_mode():
    global recognizer

    speaker.say("Ok, let me get the camera up and running.")
    open_camera()
    speaker.runAndWait()

#open camera function
def open_camera():
    global recognizer
    
    speaker.say("Opening the camera.")
    try:
        sp.run('start microsoft.windows.camera:', shell = True)
        speaker.runAndWait()

    except:

        print("Error opening the camera, is there one installed?") 
        speaker.say("Unfortunately, the camera isn't responding.")
        speaker.runAndWait()

#function for Austin to open terminal
def open_terminal():
    global recognizer
    speaker.say("Opening the terminal.")
    try:
        os.system('start cmd')
        speaker.runAndWait()
    
    except:
        print("Error opening the terminal, please try again later.")
        speaker.say("hmmm, it seems that the terminal doesn't want to open anything.")
        speaker.runAndWait()

#function for Austin to open steam
def open_steam():
    speaker.say("Ok, opening Steam.")
    try:
        os.startfile(paths["Steam"])
        speaker.runAndWait()

    except:
        speaker.say("oh, look like steam isn't working properly, please try again later.")
        print("Error, failed to open Steam. Please try again later.")
        speaker.runAndWait()

#Function to add for Hannah
def baby_mode():
    speaker.say("playing baby music...")
    play_on_youtube("https://www.youtube.com/watch?v=aQ2D0m0eFYQ&list=RDaQ2D0m0eFYQ&start_radio=1")
    speaker.runAndWait()

#Function for Austin to open code
def open_code():
    speaker.say("Ok, opening visual studio code.")
    try:
        os.startfile(paths["code"])
        speaker.runAndWait()
    
    except:
        speaker.say("oh, look like visual studio code isn't working properly, please try again later.")
        print("Error, failed to open visual studio code. Please try again later.")
        speaker.runAndWait()

def search_google():
    global recognizer
    
    speaker.say("Searching on google")
    speaker.say("What do you want to search up?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                search_term = recognizer.recognize_google(audio)
                search_term = search_term.lower()

                search_on_google(search_term)
                done = True

                speaker.say(f"Here is the results for {search_term}.")
                speaker.runAndWait()
        
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Sorry, I did not understand, could you repeat that again?")
            speaker.runAndWait()

#function to search on google
def search_on_google(query):
    pywhatkit.search(query)

#Function to search on wikipedia
def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=5)
    return results

def search_wikipedia():
    global recognizer
    
    speaker.say("Searching on Wikipedia")
    speaker.say("What do you want to search up?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                search_term = recognizer.recognize_google(audio)
                search_term = search_term.lower()

                wiki_result = search_on_wikipedia(search_term)
                done = True
                speaker.setProperty('rate', 150)
                speaker.say(wiki_result)
                speaker.setProperty('rate', 190)
                speaker.runAndWait()
        
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Sorry, I did not understand, could you repeat that again?")
            speaker.runAndWait()    

def write_keyboard():
    global recognizer
    
    speaker.say("Ok, what should I type")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                user_input = recognizer.recognize_google(audio)
                user_input = user_input.lower()

                speaker.say("Ok typing...")
                done = True
                pyautogui.write(user_input, interval= 0.1)
                speaker.runAndWait()
        
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Sorry, I did not understand, could you repeat that again?")
            speaker.runAndWait()

#Open website section

def openbrowser(link):
    webbrowser.open_new_tab(link)

def twitter():
    global recognizer

    speaker.say("Okay, opening twitter")
    openbrowser("https://twitter.com/home?lang=en")
    speaker.runAndWait()

def open_gmail():
    global recognizer
    
    speaker.say("Okay, opening gmail")
    openbrowser("https://mail.google.com/mail/?tab=rm&authuser=0&ogbl")
    speaker.runAndWait()


#Remind me to add this function later
#def send_email()

def get_latest_news():
    #Credit: https://www.freecodecamp.org/news/python-project-how-to-build-your-own-jarvis-using-python/
    news_headlines = []
    try:
        res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
        articles = res["articles"]
        for article in articles:
            news_headlines.append(article["title"])
        return news_headlines[:5]
    except:
        speaker.say("I'm sorry, currently I cannot get the latest news, please try again")
        print("Error, unable to get news, internet maybe down.")

def latest_news():
    speaker.say("Okay, getting latest news.")
    speaker.setProperty("rate", 150)
    news = get_latest_news()
    speaker.say(news)
    speaker.setProperty("rate", 190)
    speaker.runAndWait()

def get_weather_report(city):
    rest = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OpenWeatherAPI}&units=metric").json()
    weather = rest["weather"][0]["main"]
    temperature = rest["main"]["temp"]
    feels = rest["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels}℃"

def weather_report():
    
    global recognizer
    
    speaker.say("Okay, getting weather info")
    if(weatherDataBase[user] != "none"):
        speaker.setProperty("rate" , 150)
        try:
            speaker.say(get_weather_report(weatherDataBase[user]))
            speaker.setProperty("rate" , 190)
            speaker.runAndWait()
        except:
            speaker.say("Sorry, I couldn't get weather report, can you try again later?")
            speaker.runAndWait()
    else:
        speaker.say("Oh, I notice that you haven't set a city yet. Please tell me what city do you live in?")
        done = False

        while not done:
            try:
                with speech_recognition.Microphone() as mic:
                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = recognizer.listen(mic)

                    city = recognizer.recognize_google(audio)
                    city = city.lower()

                    userData[f"B{user}"] = city
                    done = True

                    speaker.say(f"Ok, I've set the city to {weatherDataBase[user]}, please try again")
                    speaker.runAndWait()
        
            except speech_recognition.UnknownValueError:
                recognizer = speech_recognition.Recognizer()
                speaker.say("Sorry, I did not understand, could you repeat that again?")
                speaker.runAndWait()

def how_to_kill_a_dead_body():   
    global recognizer

    speaker.say("Ok, so you need to find a body to kill. This can be found on your local walmart. Second, you need to do the deed. Third, hide the body, this can be done on a backyard, a fridge, or anything else that look like a human could fit in there. Last and final step, you better call saul.")
    speaker.runAndWait()

def whos_saul():
    global recognizer

    play_on_youtube("https://www.youtube.com/watch?v=jeM9yRJwKl8")
    speaker.runAndWait()

mappings = {
    "greeting": hello,
    "exit" : quit,
    "borracho_mode" : borracho_mode,
    "create_note" : create_note,
    "camera_mode" : camera_mode,
    "open_terminal" : open_terminal,
    "open_steam" : open_steam,
    "baby_mode" : baby_mode,
    "open_code" : open_code,
    "google_searches" : search_google,
    "searching_video" : search_youtube,
    "wiki_searches" : search_wikipedia,
    "keyboard" : write_keyboard,
    "twitter" : twitter,
    "web_gmail" : open_gmail,
    "introduction" : introduction,
    "get_news" : latest_news,
    "get_weather" : weather_report
}

assistant = GenericAssistant(r'intents.json', intent_methods=mappings)
assistant.train_model()
#assistant.load_model()

while True:

    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            
            message = recognizer.recognize_google(audio)
            message = message.lower()
        
        assistant.request(message)

    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()