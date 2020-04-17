import requests, json 
import speech_recognition as sr
import re
import googlemaps 
import playsound
import pyttsx3
from stt_conversion import voice
v = voice()
print(v)
engine = pyttsx3.init() 
query = v
api_key = 'AIzaSyDevDlcD-iiGG4qOs1OE8ZKsi11HTODjtA'

url = "https://maps.googleapis.com/maps/api/place/textsearch/json?" 

url2= "https://maps.googleapis.com/maps/api/place/details/json?"

r = requests.get(url + 'query=' + query +
                        '&key=' + api_key ) 
x = r.json() 

y = x['results'] 
# print(x)

# Opening Hours
pl = str(y[0]["place_id"])
name = str(y[0]["name"])
print("Place Id: ",pl)
print("Name :", name)

g = requests.get(url2 + 'place_id=' + "{}".format(pl) +   
                        '&key=' + api_key) 
j = g.json() 
l = j['result']["opening_hours"]["weekday_text"]
print(l)


#Phone NUmber
ph = requests.get(url2 + 'place_id=' + "{}".format(pl) +  '&fields=' + 'formatted_phone_number' +
                        '&key=' + api_key) 
k = ph.json()
ph_res = k['result']['formatted_phone_number']
print(ph_res)