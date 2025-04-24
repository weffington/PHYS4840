#!/usr/bin/python3.8
import numpy as np
import matplotlib.pyplot as plt

L=0.2
D=0.1
N=20
a=L/N
h=1e-5
epsilon=h/1000

def Tsurface(t):
    A=10
    B=12
    return A + B*np.sin(2*np.pi*t)

Tmid=10.0
Tdepth=11.0

tf=10
tend=tf+epsilon

T=np.empty(N+1,float)
T[0]=Tsurface(0)
T[N]=Tdepth
T[1:N]=Tmid
Tp=np.empty(N+1,float)
Tp[0]=Tsurface(0)
Tp[N]=Tdepth

t=0.0
tint=0.25
c=h*D/(a*a)

while t<tend:
    T[0]=Tsurface(t)
    Tp[0]=Tsurface(t)
    Tp[1:N]=T[1:N] + c*(T[2:N+1]+T[0:N-1]-2*T[1:N])
    T,Tp=Tp,T
    t += h
    if np.abs(t-tint)<epsilon:
        plt.plot(T)
        tint+=0.25

plt.xlabel('Depth (m)')
plt.ylabel('Temperature (°C)')
plt.title("Temperature of Earth's Crust in 3 Month Intervals")
plt.savefig('Problem2.png')
plt.show()