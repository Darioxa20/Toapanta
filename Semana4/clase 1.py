# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 08:49:04 2019

@author: 1-26-PB-L2-13
"""

class Empployee:
    empCount = 0
    def init(self, name, salary):
        self.name = name
        self.salary = salary
        Empployee.empCount += 1
        def displayCount(self):
            print("Total employee %d")%Empployee.empCount
        def displayEmployee(self):
            print("Name: {}, Salary: {}".format(self.name, self.salary))

emp1 = Empployee("Zara", 2000)
emp2 = Empployee("Manni", 5000)