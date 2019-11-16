# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 09:44:01 2019

@author: 1-26-PB-L2-13
"""
devices=[]
file=open("devices.txt","r")
for item in file:
    item=item.strip()
    devices.append(item)
file.close()
print(devices)