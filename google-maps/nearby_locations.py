import requests, json 
import speech_recognition as sr
import re
import googlemaps 
import pyttsx3
from stt_conversion import voice
# say nearby hotels , restaurants, petrol bunks etc...
api_key = 'AIzaSyDevDlcD-iiGG4qOs1OE8ZKsi11HTODjtA'
engine = pyttsx3.init() 


text = voice() 
t = str(text)
print("You said : {}".format(t))
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

query = t

r = requests.get(url + 'query=' + query +
                        '&key=' + api_key) 
x = r.json() 
y = x['results'] 
for i in range(len(y)): 

    print(y[i]['name'])
    res = y[i]['name'] 
    engine.say(res)
    engine.runAndWait()             

