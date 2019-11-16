# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 18:44:01 2019

@author: 1-26-PB-L2-13
"""

try:
    y=1/0
except ArithmeticError:
    print("Aritmetic")
except ZeroDivisionError:
    print("Zero Division")

print("End")