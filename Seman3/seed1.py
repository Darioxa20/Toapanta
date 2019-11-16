# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:10:19 2019

@author: Juan Carlos
"""

import random

print ("Random number with seed 30")
random.seed( 30 )
print ("first - ", random.randint(25,50))

#will generate a same random number as previous
random.seed( 30 )
print ("Second - ", random.randint(25,50))

#will generate a same random number as previous
random.seed( 30 )
print ("Third - ", random.randint(25,50))