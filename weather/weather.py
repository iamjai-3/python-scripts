# pip install stt_conversion
from stt_conversion import voice
import random
import speech_recognition as sr
import pyttsx3
import webbrowser
import pyowm
import requests, json 
import re

engine = pyttsx3.init() 

Weather_API_KEY = "64f270d8dc07242b28b7cdd3a6080bc0"

text = voice()

f = str(text)
print("You said : {}".format(text))
g = f.split()       
city_name = g[5]        
say = ['tell me the weather of {}'.format(city_name)]

if f in say:

    complete_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=64f270d8dc07242b28b7cdd3a6080bc0&units=metric'.format(city_name)

    response = requests.get(complete_url) 
    x = response.json() 
    temp = x['main']['temp']
    wind_speed = x['wind']['speed']

    latitude = x['coord']['lat']
    longitude = x['coord']['lon']

    description = x['weather'][0]['description']

print('Temperature : {} degree celcius'.format(temp))
print('Wind Speed : {} m/s'.format(wind_speed))
print('Latitude : {}'.format(latitude))
print('Longitude : {}'.format(longitude))
print('Description : {}'.format(description))
engine.say('Temperature : {} degree celcius'.format(temp))
engine.runAndWait()
engine.say('Description : {}'.format(description))
engine.runAndWait()











