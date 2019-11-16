# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:25:55 2019

@author: 1-26-PB-L2-13
"""
#conectar python a la nuve para obtener informacion

import urllib.parse
import requests


main_api="https://www.mapquestapi.com/directions/v2/route?"
#orig="Washington"
#dest = "Baltimaore"
key="ryl2EUo31nosUAriP3lGhGJKa9YpLo5Y"
#url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
#json_data = requests.get(url).json()
#print(json_data)

'''
print("URL: "+ (url))
json_data=requests.get(url).json()
json_status=json_data["info"]["statuscode"]

if json_status==0:
    print("Api Status"+str(json_status)+"-A succesful route call.\n ")
'''

while True:
    orig=input("Starting location ")
    dest=input("Destination: ")
    url=main_api+urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: "+ (url))