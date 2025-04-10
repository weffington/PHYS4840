#!/usr/bin/env python3.8.10
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '/home/noahh/PHYS_4840')
import my_functions_lib as mfl
def f(x,t):
    return -x**3 + np.sin(t)

t0=0
dt=0.1
x0=1
t1,x1=mfl.RK2(f,x0,t0,10,dt)
t2,x2=mfl.RK2(f,x0,t0,10000,dt)

file1='rk2_results1.dat'
file2='rk2_results2.dat'
t3,x3=np.loadtxt(file1,unpack=True,skiprows=1)
t4,x4=np.loadtxt(file2,unpack=True,skiprows=1)
fig, ax = plt.subplots(2,1,figsize=(10,12))

ax[0].plot(t1,x1,'b',linewidth=3)
ax[0].plot(t3,x3,'r')
ax[0].legend(['Python','Fortran'])
ax[0].set_xlabel('$t$')
ax[0].set_ylabel('$x(t)$')
ax[0].set_title('$[0,10]$, $dt=0.1$')
ax[0].set_xlim(0,10)
fig.suptitle('Python vs. Fortran RK2', fontsize=16)

ax[1].plot(t2,x2,'b',linewidth=3)
ax[1].plot(t4,x4,'r')
ax[1].legend(['Python','Fortran'])
ax[1].set_xlabel('$t$')
ax[1].set_ylabel('$x(t)$')
ax[1].set_title('$[0,10000]$, $dt=0.1$')
ax[1].set_xlim(0,10)

plt.savefig('Problem_2.png')
plt.show()