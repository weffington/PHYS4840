#!/usr/bin/python3.8.10
import numpy as np
import sys
sys.path.insert(0, '/home/noahh/PHYS_4840')
import my_functions_lib as mfl

#e)
def gamma(a):
    z=np.linspace(0,1,1000)
    c=a-1
    x=(c*z)/(1-z)
    y=np.where(z != 1, c*(np.exp((c*np.log(x)) - x)/((1-z)**2)), 0)
    gamma=mfl.romberg(y,z,10)
    if a==int(a):
        return round(gamma)
    else:
        return gamma
print(f"gamma(3/2): {gamma(3/2)}")

#f)
print(f"\ngamma(3): {gamma(3)}")
print(f"\ngamma(6): {gamma(6)}")
print(f"\ngamma(10): {gamma(10)}")