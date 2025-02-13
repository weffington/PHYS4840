#Homework 2 Problem 1
#Noah Hampton
#w/ major help from Chase Worsley
#(had no clue what I was doing)
import numpy as np
import matplotlib.pyplot as plt

ngc_path = 'NGC6341.dat'
mist_path = 'MIST_v1.2_feh_m1.75_afe_p0.0_vvcrit0.4_HST_WFPC2.iso.cmd'

ngc_blue, ngc_red = np.loadtxt(ngc_path, usecols=(8, 26), unpack=True)
ngc_mag = ngc_blue
ngc_color = ngc_blue - ngc_red
quality_cut=np.where((ngc_red > -99) &\
                    (ngc_blue > -99))

new_file = []
with open(mist_path, 'r') as file:
    for line in file:
        if '#' in line:
            continue
        elif not line.strip():
            continue
        else:
            new_file.append(line)

new_mist = "MIST.dat"
with open('MIST.dat', 'w') as file:
    for line in new_file:
        file.write(line)

mist_blue, mist_red = np.loadtxt(new_mist, usecols=(12, 20), unpack=True)
mist_mag = mist_blue
mist_color = mist_blue - mist_red

fig, ax = plt.subplots(figsize=(8,16))

plt.plot(ngc_color[quality_cut],ngc_mag[quality_cut],'k.',markersize=4)
plt.plot(mist_color,mist_mag,'r.',markersize=4)
plt.title('H-R Diagram for NGC6341 with MIST Isochrone', fontsize=22)
plt.xlabel('Color: B-R',fontsize=20)
plt.ylabel('Magnitude: B',fontsize=20)
plt.legend(['NGC Data','MIST Data'])
plt.xlim(-2,5)
plt.ylim(-5,25)
plt.gca().invert_yaxis()


plt.show()
plt.close()


