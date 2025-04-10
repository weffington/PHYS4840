#!/usr/bin/env python3.8.10
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
sys.path.insert(0, '/home/noahh/PHYS_4840')
import my_functions_lib as mfl

def f(x,t):
    return -x**3 + np.sin(t)

t0=0
dt=0.1
x0=1

start_RK4_1 = time.perf_counter()

t1,x1=mfl.RK4(f,x0,t0,10,dt)

end_RK4_1 = time.perf_counter()

start_RK4_2 = time.perf_counter()

t2,x2=mfl.RK4(f,x0,t0,1000,dt)

end_RK4_2 = time.perf_counter()

start_RK4 = time.perf_counter()

t,x=mfl.RK4(f,x0,t0,80,dt)

end_RK4 = time.perf_counter()
print(f"Python runtime w/ 100 steps: {end_RK4_1 - start_RK4_1}")
print(f"Python runtime w/ 10000 steps: {end_RK4_2 - start_RK4_2}")
print(end_RK4-start_RK4)

#Python 100 time steps: 0.0003735969999070221 seconds

#Python 10000 time steps: 0.0333179399999608s seconds

#Python 800 time steps: 0.003435902000092028 seconds

#Fortran 100 time steps:
#Compilation time: .048912218 seconds
#Execution time: .001865885 seconds

#Fortran 10000 time steps: 
#Compilation time: .049109816 seconds 
#Execution time: .014300188 seconds

#Fortran 800 time steps:
#Compilation time: .058718425 seconds
#Execution time: .003172601 seconds

#not counting compilation time,
#Fortran and Python are on par performance-wise
#after around 800 time steps


