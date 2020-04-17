import time
import os
import speech_recognition as sr
import re 
import json
import sys
import threading, logging
import playsound
from time import strftime

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)
handler = logging.FileHandler(strftime("Events_%H_%M_%m_%d_%Y.log"))
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def check(hour,min,sec):
    
    c= ":"
    while hour > -1:
        while min > -1:
            while sec > 0:
                sec=sec-1
                time.sleep(1)
                sec1 = ('%02.f' % sec)  # format
                min1 = ('%02.f' % min)
                hour1 = ('%02.f' % hour)
                sys.stdout.write('\r' + str(hour1) + c + str(min1) + c + str(sec1))
                logging.debug(str(hour1) + c + str(min1) + c + str(sec1))
                logger.info(str(hour1) + c + str(min1) + c + str(sec1))

                if str(hour1) == "00" and  str(min1) == "00" and str(sec1) == "07":
                    # playsound.playsound('test.mp3', True)

                    print("Time up")

            min=min-1
            sec=60
        hour=hour-1
        min=59

    print('Countdown Complete.')
      

def len1():

    if "seconds" in g:
        try:
            t1 = threading.Thread(target=check, args=(0,0,int(res[0],)), daemon = 'true')  
            logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
          
            t1.start()

            while t1.is_alive():
                t1.join(1)
           
        except KeyboardInterrupt:           
            print("\n stopped \n")
            

    elif "hours" in g:
        try:
            t2 = threading.Thread(target=check, args=(int(res[0]),0,0,), daemon = 'true')
            logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')

            t2.start()

            while t2.is_alive():
                t2.join(1)

        except KeyboardInterrupt:           
            print("\n stopped \n")
            

    elif "minutes" in g:

        try:
            t3 = threading.Thread(target=check, args=(0,int(res[0]),0,), daemon = 'true')
            t3.start()

            while t3.is_alive():
                t3.join(1)

        except KeyboardInterrupt:           
            print("\n stopped \n")
            

def len2():
    if "hours" and "hour" in g:
        try:
            t4 = threading.Thread(target=check, args=(int(res[0]),int(res[1]),0,), daemon = 'true')
            t4.start()

            while t4.is_alive():
                t4.join(1)
        
        except KeyboardInterrupt:        
            print("\n stopped \n")
            
          
    elif "minutes" or "minute" in g:
        try:
            t5 = threading.Thread(target=check, args=(0,int(res[0]),int(res[1],)), daemon = 'true') 
            t5.start()

            while t5.is_alive():
                t5.join(1)
        
        except KeyboardInterrupt:           
            print("\n stopped \n")


while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:    
        print("Speak Anything :")
        audio = r.listen(source)       
        try:
            text = r.recognize_google(audio)   
            t = str(text)
            print("You said : {}".format(t)) 
            res = [int(i) for i in t.split() if i.isdigit()] 
            res_len = len(res)         
            g = str(t.split())
            
            if res_len == 1:
               t6 = threading.Thread(target=len1, args=(), daemon = 'true') 
               t6.start()
      
            elif res_len == 2:
               t7= threading.Thread(target=len1, args=(), daemon = 'true') 
               t7.start()

            if t == "my timers":
                print(int(threading.active_count()/2))

            # print(str(g[1]))      
                #check()
        except:
            print("Sorry could not recognize your voice") 

            

      
      

       
