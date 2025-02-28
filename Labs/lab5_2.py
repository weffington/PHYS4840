#!/usr/bin/env python3.10.12
####################################################
#
# Author: M Joyce
#
####################################################
import numpy as np
import matplotlib.pyplot as plt
import sys
import my_functions_lib as mfl

################################################
#
# Homework 2 problem 1 help
# Part 2
#
# Now, let's compare this to the HST data 
#
#################################################


'''
This code block loads and cleans the theoretical models from
the iso.cmd file. It is the same code as in isochrone_in-class_demo.py
but with the comments and instructions removed. Consult the commented 
version of this file if you are confused about any of these steps 
'''
load_file = 'MIST_v1.2_feh_m1.75_afe_p0.0_vvcrit0.4_HST_WFPC2.iso.cmd'

log10_isochrone_age_yr, F606, F814,\
logL, logTeff, phase= np.loadtxt(load_file, usecols=(1,14,18,6,4,22), unpack=True, skiprows=14)

age_Gyr_1e9 = (10.0**log10_isochrone_age_yr)/1e9
age_Gyr = age_Gyr_1e9

age_selection = np.where((age_Gyr > 12) & (age_Gyr <= 13.8)) 

color_selected = F606[age_selection]-F814[age_selection]
magnitude_selected = F606[age_selection]

Teff = 10.0**logTeff
Teff_for_desired_ages =  Teff[age_selection]
logL_for_desired_ages =  logL[age_selection]

phases_for_desired_age = phase[age_selection]
desired_phases = np.where(phases_for_desired_age <= 3)

## now, we can restrict our equal-sized arrays by phase
cleaned_color = color_selected[desired_phases]
cleaned_magnitude = magnitude_selected[desired_phases]
cleaned_Teff = Teff_for_desired_ages[desired_phases]
cleaned_logL = logL_for_desired_ages[desired_phases]

####################################################################

'''
Now, recall how we loaded, cleaned, and plotted NGC6341.dat
'''
filename = 'NGC6341.dat'

## # Col.  9: F336W calibrated magnitude
## # Col. 15: F438W calibrated magnitude
## # Col. 27: F814W calibrated magnitude
## # Col. 33: membership probability
## but Python indexes from 0, not 1!

blue, green, red, probability = np.loadtxt(filename, usecols=(8, 14, 26, 32), unpack=True)
mu=mfl.dmodulus(8630)
magnitude=blue-mu
color = blue - red

quality_cut = np.where( (red   > -99.) &\
					    (blue  > -99)  &\
					    (green > -99)  &\
					    (probability != -1))
 
print("quality_cut: ", quality_cut )


fig, ax = plt.subplots(figsize=(8,16))

plt.plot(color[quality_cut], magnitude[quality_cut], "k.", markersize = 4, alpha = 0.2)
plt.plot(cleaned_color,cleaned_magnitude)
plt.gca().invert_yaxis()
plt.xlabel("Color: B-R", fontsize=20)
plt.ylabel("Magnitude: B", fontsize=20)
plt.title('Hubble Space Telescope Data for\nthe Globular Cluster NGC6341', fontsize=22)
plt.xlim(-2, 4)
plt.ylim(10.5,-2)
plt.show()
plt.close()
#from the plot, we can conclude that this isochrone model is not a good fit for our data