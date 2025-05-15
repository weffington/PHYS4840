#!/usr/bin/python3.8
#####################################
#
# Class 26: Oddball integration
# Author: Mark Newman, modified by M Joyce
#
#####################################

from math import sqrt,log,cos,sin,pi
from random import random
import time

start=time.perf_counter()
Z = 79
e = 1.602e-19
E = 7.7e6*e
epsilon0 = 8.854e-12
a0 = 5.292e-11
sigma = a0/100

N = int(1e7)

def gaussian():
    r = sqrt(-2*sigma*sigma*log(1-random()))
    theta = 2*pi*random()
    x = r*cos(theta)
    y = r*sin(theta)
    return x,y

count = 0
for i in range(N):
    x,y = gaussian()
    b = sqrt(x*x+y*y)
    if b<Z*e*e/(2*pi*epsilon0*E):
        count += 1
end=time.perf_counter()
print(count,"particles were reflected out of",N)
print(end-start)

#Python:
#1e6 particles: 0.6964982000063173 sec
#1e7 particles: 6.291228500020225 sec

#Fortran:
#1e6 particles:
#Compilation time: .053505718 seconds
#Execution time: .052702884 seconds

#1e7 particles:
#Compilation time: .072870669 seconds
#Execution time: .408279887 seconds
