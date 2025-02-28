#!/usr/bin/env python3.10.12
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




