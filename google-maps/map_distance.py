import speech_recognition as sr
import re
import googlemaps 
import pyttsx3
from stt_conversion import voice

gmaps = googlemaps.Client(key='AIzaSyDevDlcD-iiGG4qOs1OE8ZKsi11HTODjtA') 
engine = pyttsx3.init() 
  # Say distance between {loc1} and {loc2}

text = voice() 
t = str(text)
print("You said : {}".format(t))               
g = t.split()     
city = g 
start = g[2]
dest = g[4]      
my_dist = gmaps.distance_matrix(start, dest)['rows'][0]['elements'][0] 

distance = my_dist['distance']['text']
duration = my_dist['duration']['text']

print(distance)
print(duration)


engine.say('Distance is : {}'.format(distance))
engine.runAndWait()
engine.say('Duration : {}'.format(duration))
engine.runAndWait()
