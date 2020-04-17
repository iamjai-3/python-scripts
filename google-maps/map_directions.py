import googlemaps
from datetime import datetime
import pprint
import json

import speech_recognition as sr
import re
import googlemaps 

gmaps = googlemaps.Client(key='AIzaSyDevDlcD-iiGG4qOs1OE8ZKsi11HTODjtA')

  
r = sr.Recognizer()
with sr.Microphone() as source:    
    print("Speak Anything :")
    audio = r.listen(source)       
    try:
        text = r.recognize_google(audio)   
        t = str(text)
        print("You said : {}".format(t)) 
        dir = t.split()
        start_point = dir[2]
        end_point = dir[4]
        now = datetime.now()
        directions_result = gmaps.directions(start_point,
                                        end_point,
                                        mode="driving",
                                        departure_time=now)

        for leg in directions_result[0]['legs']:
            startAddress = leg['start_address']
            print ("Start Address:", startAddress)
            endAddress = leg['end_address']
            print ("End Address:", endAddress)
            distance=leg['distance']['text']
            print ("Distance:",distance)
            duration=leg['duration']['text']
            print ("Duration:",duration)

            for step in leg['steps']:
                html_instructions = step['html_instructions']
                instr= step['distance']['text']
                instrtime=step['duration']['text']
                print (html_instructions + " " +instr+ " " + instrtime)

                if 'steps' in step:
                    
                    for stepp in step['steps']:
                        y=stepp['html_instructions']
                        print(y)

       
    except:
        print("Sorry could not recognize your voice") 

