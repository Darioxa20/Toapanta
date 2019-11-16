# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 19:18:44 2019

@author: 1-26-PB-L2-13
"""




def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        c=a+b
        a=b
        b=c
        #a, b = b, a+b # Asignacion Multiple variable
    print()
#fib(100)  

'''
def fibo(n1):
    if n1 < 2:
        return n1
    else:       
        return fibo(n1-1) + fibo(n1-2)
    
fibo(30)'''