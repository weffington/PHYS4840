#!/usr/bin/env python3.10.12
import numpy as np
x=range(1,5)
print(x)
#a)
def f(x):
    y=np.square(x)
    return y

def squareSum(x):
    y=f(x)
    sum=np.sum(y)
    return sum
print(squareSum(x))

#b)
def avg(x):
    avg=(np.sum(x))/len(x)
    return avg
print(avg(x))

#c)
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))


