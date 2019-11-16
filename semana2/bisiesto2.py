# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:03:24 2019

@author: 1-26-PB-L2-13
"""
year=int(input("Año:"))

valor=false
if(year%4==0):
    valor=True
if(year%100==0):
    valor=False
    if(year%400==0):
        valor=True
return valor