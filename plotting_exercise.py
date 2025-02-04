#!/usr/bin/python3.10.12
#####################################
#
# Class 5: Linear and Log + Plotting
# Author: Noah Hampton
#
#####################################
import numpy as np
import matplotlib.pyplot as plt

## in your functions library, which should 
## be in a different file, define the function
#
# def y(x):
# 	y = 2.0*x**3.0
# 	return y
#
# and import your functions library

import my_functions_lib as mfl

# define your x values
x = np.linspace(1, 100, 500)  # x values

y = mfl.y(x) # complete this statement using the
		# function you wrote in your functions library

# (1) make a linear plot of y vs x
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
plt.close()
# (2) make a log-log plot of y vs x
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()
plt.close()
# (3) make a plot of log(x) vs log(y)
logx=np.log10(x)
logy=np.log10(y)
plt.plot(logx,logy)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
plt.close()