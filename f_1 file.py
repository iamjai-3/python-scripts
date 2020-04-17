# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:20:21 2020

@author: ASUS
"""

def text(input):
    input = input.lower()
    split_km=input.split('to')
    input_1=split_km[0].replace("convert","").strip()
    #print(input_1)
    value_to_be_converted=input_1.split()[0]
    #print(value_to_be_converted)
    unit_1=input_1.split()[1]
    unit_2=split_km[1].strip()
    #print(value_to_be_converted)
    #print(unit_1)
    #print(unit_2)
   # convertions(unit_1, unit_2, value_to_be_converted)
def convertion(unit_1,unit_2,val)  :
    
        

    if(unit_1 in ["kilometers", "km", "kms", "kilometer"] and unit_2 in ["miles", "miles"]):
       
       #if(unit_2 in ["miles", "miles"]):
       final = float(val) * 0.6231
       print(str(val) + " " + unit_1 + " in " + unit_2 + " is " + str(final))
    elif(unit_1 in ["miles", "mile"] and unit_2 in ["kilometers", "kilometer","km"]):
       #elif(unit_2 in ["kilometers", "kilometer","km"]):
       final = float(val) * 1.609344
       print(str(val) + " " + unit_1 + " in " + unit_2 + " is " + str(final))
    elif(unit_1 in ["celsius", "c"] and unit_2 in ["fahrenheit", "fahreinheits"]):
       #if(unit_2 in ["fahrenheit", "fahreinheits"]):
           final =  9.0/5.0*float(val) +32
           print(str(val) + " " + unit_1 + " in " + unit_2 + " is " + str(final))
    elif(unit_1 in ["fahrenheits", "fahrenheit"] and unit_2 in ["celsius", "c"]):
       #if(unit_2 in ["celsius", "c"]):
           final = (float(val)-32) * 5.0/9.0
           print(str(val) + " " + unit_1 + " in " + unit_2 + " is " + str(final))
    elif(unit_1 in ["meters", "meter"] and unit_2 in ["feets", "feet"]):
       #if(unit_2 in ["feets", "feet"]):
           final = float(val) * 3.28084
           print(str(val) + " " + unit_1 + " in " + unit_2 + " is " + str(final))
    elif(unit_1 in ["feets", "feet"] and unit_2 in ["meeters", "meeter"]):
       #if(unit_2 in ["meeters", "meeter"]):
           final = float(val) * 0.3048
           print(str(val) + " " + unit_1 + " in " + unit_2 + " is " + str(final))
    elif(unit_1 in ["inche", "inches"] and unit_2 in ["centemeter", "centemeters","cm"]):
       #if(unit_2 in ["centemeter", "centemeters","cm"]):
           final = float(val) * 0.39370 
           print(str(val) + " " + unit_1 + " in " + unit_2 + " is " + str(final))
    elif(unit_1 in ["centemeters", "centemeter", "cm"] and unit_2 in ["inches", "inche"]):
       #if(unit_2 in ["inches", "inche"]):
           final = float(val) / 2.54 
           print(str(val) + " " + unit_1 + " in " + unit_2 + " is " + str(final))
    elif(unit_1 in ["inches", "inche"] and unit_2 in ["milimeters","millimeter", "mm"]):
       #if(unit_2 in ["milimeters","millimeter", "mm"]):
           final = float(val) * 0.6256
           print(str(val) + " " + unit_1 + " in " + unit_2 + " is " + str(final))
    elif(unit_1 in ["millimeter", "millimeters","mm"] and unit_2 in ["inches", "inche"]):
       #if(unit_2 in ["inches", "inche"]):
           final = float(val) * 0.0393701
           print(str(val) + " " + unit_1 + " in " + unit_2 + " is " + str(final))
    elif(unit_1 in ["kilograms", "kg", "kgs", "kilogram"] and unit_2 in ["pound", "pounds"]):
       #if(unit_2 in ["pound", "pounds"]):
           final = float(val) * 2.20462
           print(str(val) + " " + unit_1 + " in " + unit_2 + " is " + str(final))
    elif(unit_1 in ["pounds", "pound"] and unit_2 in ["kilograms", "kilogram","kg","kgs"] ):
       #if(unit_2 in ["kilograms", "kilogram","kg","kgs"]):
           final = float(val) * 0.454
           print(str(val) + " " + unit_1 + " in " + unit_2 + " is " + str(final))
    elif(unit_1 in ["inches", "inche"] and unit_2 in ["feets", "feet"]):
       #if(unit_2 in ["feets", "feet"]):
           final = float(val) * 0.0833333333 
           print(str(val) + " " + unit_1 + " in " + unit_2 + " is " + str(final))
    elif(unit_1 in ["feets", "feet"] and unit_2 in ["inches", "inches"]):
       #if(unit_2 in ["inches", "inches"]):
           final = float(val) * 12 
           print(str(val) + " " + unit_1 + " in " + unit_2 + " is " + str(final))
    elif(unit_1 in ["miles per hour", "mph"] and unit_2 in ["kilometers per hour", "kph"]):
       #if(unit_2 in ["kilometers per hour", "kph"]):
           final = float(val) * 1.609344 
           print(str(val) + " " + unit_1 + " in " + unit_2 + " is " + str(final))
    elif(unit_1 in ["kilometer per hour", "kph"] and unit_2 in ["miles per hour", "mph"]):
       #if(unit_2 in ["miles per hour", "mph"]):
           final = float(val) * 0.6213711922
           print(str(val) + " " + unit_1 + " in " + unit_2 + " is " + str(final))
    else:
        print("none")
    
   
text("Convert 3 mph to kph")
