# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 18:54:52 2019

@author: 1-26-PB-L2-13
"""


def badFun(n):
    try:
        return n/0
    except:
        print("I did it again")
    raise
try:
    badFun(0)
except ArithmeticError:
        print("I see")
print("The end")