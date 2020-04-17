# import time
# import os
# import speech_recognition as sr
# import re 
# import json
# import sys

# def check(hour,min,sec):
    
#     c= ":"
#     while hour > -1:
#         while min > -1:
#             while sec > 0:
#                 sec=sec-1
#                 time.sleep(1)
#                 sec1 = ('%02.f' % sec)  # format
#                 min1 = ('%02.f' % min)
#                 hour1 = ('%02.f' % hour)
#                 sys.stdout.write('\r' + str(hour1) + c + str(min1) + c + str(sec1))
#                 if str(hour1) == "00" and  str(min1) == "00" and str(sec1) == "05":
#                     print("Time up")

#             min=min-1
#             sec=60
#         hour=hour-1
#         min=59

#     print('Countdown Complete.')
 

# r = sr.Recognizer()
# with sr.Microphone() as source:    
#     print("Speak Anything :")
#     audio = r.listen(source)       
#     try:
#         text = r.recognize_google(audio)   
#         t = str(text)
#         print("You said : {}".format(t))
#         print(t)
#         res = [int(i) for i in t.split() if i.isdigit()] 
#         res_len = len(res)
#         print(res_len)
#         g = str(t.split())
#         # print(str(g[1]))      
#             #check()
#     except:
#         print("Sorry could not recognize your voice") 
       



# # if g[1] == "seconds":
# #     check(0,0,int(g[0]))

# # elif g[1] == "minutes":
# #      check(0,int(g[0]),0)

# # elif g[1] == "hours":
# #      check(int(g[0]),0,0)

# # else:
# #     print("Set Timer")


# if res_len == 1:

#     if "seconds" in g:
#         check(0,0,int(res[0]))
    
#     elif "hours" in g:
#         check(int(res[0]),0,0)

#     elif "minutes" in g:
#         check(0,int(res[0]),0)
      

# elif res_len == 2:

#     if "hours" and "hour" in g:
#         check(int(res[0]),int(res[1]),0)

#     elif "minutes" or "minute" in g:
#         check(0,int(res[0]),int(res[1]))
      
from timer_mod import check

check(5,2,4)