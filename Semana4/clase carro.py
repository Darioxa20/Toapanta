# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 08:58:01 2019

@author: 1-26-PB-L2-13
"""

class Car():
 """A simple attempt to model a car."""

 def __init__(self, make, model, year):

     self.make = make
     self.model = model
     self.year = year
 # Fuel capacity and level in gallons.
     self.fuel_capacity = 15
     self.fuel_level = 0
 def fill_tank(self):

     self.fuel_level = self.fuel_capacity
     print("Fuel tank is full.")

 def drive(self):

     print("The car is moving.")