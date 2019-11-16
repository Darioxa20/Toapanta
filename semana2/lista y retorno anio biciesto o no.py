# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 08:45:02 2019

@author: 1-26-PB-L2-13
"""

def isYearLeap(year):
#
# Su codigo 
#
'''if (year!=0):
    if(year%4==0):
        print("Año Bisiesto")
    else:
        print("No Bisiesto")
elif(year%400==0)
print("Bisiesto")

else:
    print(No bisiesto)
'''

    
    
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
