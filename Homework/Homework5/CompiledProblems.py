#!/usr/bin/env python3.8.10
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
sys.path.insert(0, '/home/noahh/PHYS_4840')
import my_functions_lib as mfl
#used Prof. Joyce's RK2 and RK4 function templates in 
#my_functions_lib

#Problem 1
def V_in(t):
    if np.floor(2*t)%2==0:
        return 1
    else:
        return -1
def f(V_out,t,RC):
    return (1/RC)*(V_in(t)-V_out)
RC=[0.01,0.1,1]
t0=0
tf=10
V_out=0
N=10000
dt=(tf-t0)/N

tpoints=np.arange(t0,tf,dt)
Vfctns=[]
for i in range(3):
    Vpoints=[]
    for t in tpoints:
        Vpoints.append(V_out)
        k1 = dt*f(V_out,t,RC[i])
        k2 = dt*f(V_out+0.5*k1,t+0.5*dt,RC[i])
        k3 = dt*f(V_out+0.5*k2,t+0.5*dt,RC[i])
        k4 = dt*f(V_out+k3,t+dt,RC[i])
        V_out += (k1 + 2*k2 + 2*k3 + k4)/6
    Vfctns.append(Vpoints)

fig, ax=plt.subplots(1,3,figsize=(20,5))
for j in range(len(Vfctns)):
    ax[j].plot(tpoints,Vfctns[j])
    ax[j].set_xlabel('$t$')
    ax[j].set_ylabel('$V_{out}$')
ax[0].set_title('$RC=0.01$')
ax[1].set_title('$RC=0.1$')
ax[2].set_title('$RC=1$')
plt.savefig('Problem_1.png')
plt.show()

#Problem 2
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

#Problem 3
def f(x,t):
    return -x**3 + np.sin(t)

t0=0
dt=0.1
x0=1
t1,x1=mfl.RK4(f,x0,t0,10,dt)
t2,x2=mfl.RK4(f,x0,t0,10000,dt)

file1='rk4_results1.dat'
file2='rk4_results2.dat'
t3,x3=np.loadtxt(file1,unpack=True,skiprows=1)
t4,x4=np.loadtxt(file2,unpack=True,skiprows=1)
fig, ax = plt.subplots(2,1,figsize=(10,12))

ax[0].plot(t1,x1,'b')
ax[0].plot(t3,x3,'r')
ax[0].legend(['Python','Fortran'])
ax[0].set_xlabel('$t$')
ax[0].set_ylabel('$x(t)$')
ax[0].set_title('$[0,10]$, $dt=0.1$')
ax[0].set_xlim(0,10)
fig.suptitle('Python vs. Fortran RK4', fontsize=16)

ax[1].plot(t2,x2,'b')
ax[1].plot(t4,x4,'r')
ax[1].legend(['Python','Fortran'])
ax[1].set_xlabel('$t$')
ax[1].set_ylabel('$x(t)$')
ax[1].set_title('$[0,10000]$, $dt=0.1$')
ax[1].set_xlim(0,10)

plt.savefig('Problem_3.png')
plt.show()

#Problem 4
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


