# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:11:38 2019

@author: 1-26-PB-L2-13
"""

def isYearLeap(year):
#
# your code from LAB 4.1.3.6
#
    if year!=0 and year>0:         
        return True
    else:
        return False
    
def daysInMonth(year, month):
#
# put your new code here
#
    if month!=0 and month<13:
        print("Bien")
        return True
    else:
        print("Mal")
        return False

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 12, 13]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
