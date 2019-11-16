# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 18:48:57 2019

@author: 1-26-PB-L2-13
"""

def badFun(n):
    try:
        return 1/n
    except ArithmeticError:
        print("Arithmetic Problem")
    return None
badFun(0)
print("The end") 