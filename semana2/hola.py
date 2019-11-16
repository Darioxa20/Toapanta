# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 19:06:38 2019

@author: 1-26-PB-L2-13
"""
#1 solucion
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
print (isPrime(15))

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()

print("")
#2 solucion

def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True
for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()