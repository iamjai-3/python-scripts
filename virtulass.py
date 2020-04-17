import requests
import datetime
import random
import sys
import os
import webbrowser
import urllib
import pyttsx3
import speech_recognition as sr
import pyaudio
from PyDictionary import PyDictionary
# from pygame import mixer
from googlesearch import search

# import ety
# from nltk.corpus import wordnet

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 1].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-62)     # Slows down theprinting speed of the engine voice.

# defprint(audio):
#     print("Nova: "+audio)
#     engine.say(audio)
#     engine.runAndWait()

def command():
    cmd = sr.Recognizer()
    with sr.Microphone() as source:
        cmd.adjust_for_ambient_noise(source)    # Adjusts the level to recieve voice even in case of noise in surroundings
        print('Listening..')
        audio = cmd.listen(source)
        try:
            query = cmd.recognize_google(audio,language='en-in')
            print('User: '+query+'\n')
        except sr.UnknownValueError:
            print('Sorry ! I did not get that. Could you please type it out ?')
            query = str(input('Command: '))
    return query


# def greeting():
#     currentH = int(datetime.datetime.now().hour)
#     if currentH >= 0 and currentH < 12 :
#        print('Good Morning')
#     if currentH >= 12 and currentH < 17 :
#        print('Good Afternoon')
#     if currentH >= 17 and currentH != 0 :
#        print('Good Evening')


# def playMusic():
#     music_folder = r"your music folder here"
#     music = os.listdir(music_folder)
#     random_music = music_folder + random.choice(music)
#     mixer.init()
#     mixer.music.load(random_music)
#     mixer.music.play()
    
    
# def find(name, path):
#     for root, files in os.walk(path):
#         if name in files:
#             return os.path.join(root, name)


def searchOnGoogle(query, outputList):
    print('The top five search results from Google  are listed below.')
    for output in search(query, tld="co.in", num=10, stop=5, pause=2):
        print(output)
        outputList.append(output)
    return outputList


def openLink(outputList):
    print("Here's the first link for you.")
    webbrowser.open(outputList[0])


def playOnYoutube(query_string):
    query_string = urllib.parse.urlencode({"search_query" : query})
    search_string = str("http://www.youtube.com/results?" + query_string)
    print("Here's what you asked for. Enjoy!")
    webbrowser.open_new_tab(search_string)


def tellAJoke():
    res = requests.get(
        'https://icanhazdadjoke.com/',
        headers={"Accept":"application/json"}
        )
    if res.status_code == 200:
       print("Okay. Here's one")
       print(str(res.json()['joke']))
    else:
       print('Oops!I ran out of jokes')

def getCompleteInfo(word):
    dictionary = PyDictionary()
    mean = {}
    mean = dictionary.meaning(word)
    synonyms = []
    antonyms = []

    print("Alright. Here is the information you asked for.")

    for key in mean.keys():
        print("When "+str(word)+" is used as a "+str(key)+" then it has the following meanings")
        for val in mean[key]:
            print(val)
        


    print("The possible synonyms and antonyms of "+str(word)+" are given below.")
    for syn in wordnet.synsets(word): 
        for l in syn.lemmas():
            if l.name() not in synonyms:
                synonyms.append(l.name())
            if l.antonyms() and l.antonyms()[0].name() not in antonyms:
                antonyms.append(l.antonyms()[0].name())
    
    print("Synonyms: ", end = " ")
    print(' '.join(synonyms), end = " ")
    print("\n")
    print("Antonyms: ", end = " ")
    print(' '.join(antonyms), end = " ") 
    print("\n")

    ori = ety.origins(word)
    if len(ori) > 0:
        print("There are "+str(len(ori))+" possible origins found.")
        for origin in ori:
            print(origin)
    else:
        print("I'm sorry. No data regarding the origin of "+str(word)+" was found.")


# greeting()
#print('Nova here.')
#print('What would you like me to do for you ?')



while True:

        query = command()
        query = query.lower()


        # if 'play music' in query or 'play a song' in query :
        #     print("Here's your music. Enjoy !")
        #      playMusic()
            
        # if 'stop the music' in query or 'stop the song' in query or 'stop' in query :
        #     mixer.music.stop()
        #    print('The music is stopped.')

        # if 'find file' in query:
        #    print('What is the name of the file that I should find ?')
        #     query = command()
        #     filename = query
        #     print(filename)
        #    print('What would be the extension of the file ?')
        #     query = command()
        #     query = query.lower()
        #     extension = query
        #     print(extension)
        #     fullname = str(filename) + '.' + str(extension)
        #     print(fullname)
        #     path = r'D:\\'
        #     location = find(fullname,path)
        #    print('File is found at the below location')
        #     print(location)

        if 'search' in query:
            outputList = []
            print('What should I search for ?')
            query = command()
            searchOnGoogle(query, outputList)
            print('Should I open up the first link for you ?')
            query = command()
            if 'yes' in query or 'sure' in query:
                openLink(outputList)
            if 'no' in query:
               print('Alright.')

        if 'play on youtube' in query:
            print('What should I look up for ?')
            query = command()
            playOnYoutube(query)            

        if 'open dictionary' in query or 'dictionary' in query:
            print('What word should I look up for ?')
            word = command()
            getCompleteInfo(word)
       
        if 'joke' in query:
            tellAJoke()
        
        if 'that would be all' in query or 'that is it' in query or 'bye Nova' in query:
            print('Alright. Have a nice day')
            sys.exit()    
        