import random
import speech_recognition as sr
import pyttsx3
import webbrowser
import pyowm
import requests, json 
import re


Weather_API_KEY = "64f270d8dc07242b28b7cdd3a6080bc0"

city_name = "chennai"

complete_url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid=64f270d8dc07242b28b7cdd3a6080bc0&units=metric'.format(city_name)

response = requests.get(complete_url) 
x = response.json() 

print(x)