#!/usr/bin/python3.8.10
import numpy as np
import matplotlib.pyplot as plt
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