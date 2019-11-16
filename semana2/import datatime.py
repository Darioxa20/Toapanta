# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:41:40 2019

@author: 1-26-PB-L2-13
"""
'''
import datetime
oTime=datetime.datetime.now()
print(oTime.isoFormat())'''

from math import e,exp,log,ceil,floor,trunc
print(pow(e,1)==exp(log(e)))
print(pow(2,2)==exp(2*log(2)))

x=1.4
y=1.8
print(floor(x),floor(y))
print(floor(-x),floor(-y))
print(ceil(x),ceil(y))
print(ceil(-x),ceil(-y))
print(trunc(x),trunc(y))
print(trunc(-x),trunc(-y))

