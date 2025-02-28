#!/usr/bin/env python3.10.12
#Noah Hampton
#Problem 1
#a)
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('../')
import my_functions_lib as mfl
from scipy import interpolate
file1='GAIA_G.csv'
file2='vega_SED.csv'

x, y=np.loadtxt(file1, delimiter=',', usecols=(0,1),unpack=True)
wavelength, flux = np.loadtxt(file2, delimiter=',', skiprows=1, usecols=(0,1), unpack=True)
N=1000
order=8
gaia_t=mfl.trapezoidal(y,x,N)
gaia_s=mfl.simpsons(y,x,N)
gaia_r=mfl.romberg(y,x,order)

interp_func=interpolate.interp1d(wavelength,flux,kind='linear',fill_value='extrapolate')
interp_wave=np.linspace(min(wavelength),max(wavelength),len(wavelength))
interp_flux=interp_func(interp_wave)

vega_t=mfl.trapezoidal(interp_flux,interp_wave,N)
vega_s=mfl.simpsons(interp_flux,interp_wave,N)
vega_r=mfl.romberg(interp_flux,interp_wave,15)
print('GAIA.csv integral approximations:')
print(f"Trapezoidal sum: {gaia_t}")
print(f"Simpson sum: {gaia_s}")
print(f"Romberg sum: {gaia_r}")
print("\n")
print('vega.csv integral approximations:')
print(f"Trapezoidal sum: {vega_t}")
print(f"Simpson sum: {vega_s}")
print(f"Romberg sum: {vega_r}")

#Problem 3
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

#Problem 4
def f(x):
    epsilon=10e-10
    x=np.array(x)
    y=np.where(np.abs(x)<epsilon, 1, (np.sin(x)/x)**2)
    return y

def step(x1,x2,f1,f2):
    eps=10e-4
    h1=x2-x1
    h2=h1/2
    delta = eps/(x2-x1)
    I1=(h1/2)*(f1+f2)
    I2=(h2/2)*((f1+f2) + 2*f(x1+h2))
    error=abs((I2-I1)/3)
    xmid=(x2+x1)/2
    fmid=f(xmid)
    points.append(xmid)
    if error<=(h1*delta):
        return I2
    else:
        return step(x1,xmid,f1,fmid)+step(xmid,x2,fmid,f2)
points=[]
result=step(0,10,f(0),f(10))
print(result)
x=np.linspace(0,10,1000)
plt.plot(x,f(x),'r')
plt.plot(points,f(points),'.k')
plt.title('Slice Endpoints for Adaptive Trapezoidal Approximation')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend([r"$\frac{sin^2(x)}{x^2}$",'slice endpoints' ])
plt.show()
plt.close()
