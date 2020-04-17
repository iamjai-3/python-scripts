import time
import os
import speech_recognition as sr
import re 
import json
import sys
import threading
import playsound
import yaml


def tm(t):
    time.sleep(t)
    print("process done")

while True:

    r = sr.Recognizer()
    with sr.Microphone() as source:    
        print("Speak Anything :")
        audio = r.listen(source)       
        try:
            text = r.recognize_google(audio)   
            t = str(text)
            print("You said : {}".format(t))
            print(t)
            g = t.split()
            res = [int(i) for i in t.split() if i.isdigit()] 

            
            with open(r'tst.yaml') as file:
                documents = yaml.full_load(file)

                for item, doc in documents.items():                  

                    if t in doc:
                        print("match")



    # if doc[1] == t:
    #     print("found")

            # t1 = threading.Thread(target=tm, args=(5,), daemon = 'true') 
            # t1.start()
            # playsound.playsound('test.mp3', True)

            # print("The numbers list is : " + str(res)) 
            #print(str(g[1]))      
                #check()
        except:
            print("Sorry could not recognize your voice") 

# res = [int(i) for i in t.split() if i.isdigit()] 
# print("The numbers list is : " + str(res)) 

