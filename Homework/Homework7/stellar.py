#!/usr/bin/python3.8
import numpy as np
import matplotlib.pyplot as plt
file="profile.dat"

x,y=np.loadtxt(file, unpack=True, skiprows=1)

plt.plot(x,y)
plt.savefig('stellar.png')
plt.show()
