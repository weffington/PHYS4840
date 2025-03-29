#!/usr/bin/env python3.8.10
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '/home/noahh/PHYS_4840')
import my_functions_lib as mfl
def f(x,t):
    return -x**3 + np.sin(t)
def g(x,t):
    return x**2 - x
t0=0
t_end=10
N=1000
dt = (t_end-t0)/N
x0=0
x0_1=0.5
t,x=mfl.euler_method(f,x0,t0,t_end,dt)
t1,y = mfl.euler_method(g,x0_1,t0,t_end,dt)
plt.plot(t,x,t1,y)
plt.xlabel("$t$")
plt.ylabel("$x$")
plt.legend(["$x'(t)=-x^3 + \sin{t}$",
            "$x'(t)=x^2 - x$"])
plt.show()
plt.close()