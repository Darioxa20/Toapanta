# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 18:34:42 2019

@author: 1-26-PB-L2-13
"""

try:
    x=int(input("Enter a number:"))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry")
except ValueError:
    print("You must never")
except:
    print("Oh dear, something went wrong")
print("The End")