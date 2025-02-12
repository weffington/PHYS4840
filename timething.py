#!/usr/bin/env python3.10.12
import time
import numpy as np
import sys
import pandas as pd
filename = 'NGC6341.dat'

#loadtxt
start_numpy = time.perf_counter()
blue, green, red, probability = np.loadtxt(filename,\
                 usecols=(8, 14, 26, 32), unpack=True)
print("len(green): ", len(green))
#0.15435597200030315 sec.

end_numpy  = time.perf_counter()
print('Time to run loadtxt version: ', end_numpy-start_numpy, ' seconds')
#0.15435597200030315 sec.

#parser
start_numpy = time.perf_counter()
blue, green, red = [], [], []
with open(filename, 'r') as file:
    for line in file:
        # Skip lines that start with '#'
        if line.startswith('#'):
            continue
        
        # Split the line into columns based on spaces
        columns = line.split()
        
        blue.append(float(columns[8]))   # Column 9 
        green.append(float(columns[14])) # Column 15 
        red.append(float(columns[26]))   # Column 27 

blue = np.array(blue)
green = np.array(green)
red = np.array(red)

print("len(green): ", len(green))

end_numpy = time.perf_counter()
print('Time to run parser version: ', end_numpy-start_numpy, ' seconds')
#0.3713765439997587 sec.

#pandas
start_numpy=time.perf_counter()
df = pd.read_csv(filename, delim_whitespace=True, comment='#', header=None, skiprows=54)

# Extract the columns corresponding to
# F336W, F438W, and F814W magnitudes
blue = df.iloc[:, 8]   # Column 9 
green = df.iloc[:, 14]  # Column 15 
red = df.iloc[:, 26]   # Column 27 

blue = blue.to_numpy()
green = green.to_numpy()
red = red.to_numpy()
print("len(green):", len(green))
end_numpy = time.perf_counter()
print('Time to run pandas version: ', end_numpy-start_numpy, ' seconds')
#0.6411497279996183 sec