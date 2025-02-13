#! /usr/bin/python3.10.12
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-100,100,10000)
y = x**4
logy=np.log(y)
ylog = np.log(x**4)

fig, ax=plt.subplots(1,3,figsize=(15,5))

ax[0].plot(x,y,'r-')
ax[0].set_title('$y=x^4')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[0].grid(True)

ax[1].plot(x,y,'b-')
ax[1].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_title('Log-log of $y=x^4$')
ax[1].set_xlabel('log(x)')
ax[1].set_ylabel('log(y)')
ax[1].grid(True,which='both')

ax[2].plot(x,logy,'g-')
ax[2].set_title('$log_{10}(y)$')
ax[2].set_xlabel('x')
ax[2].set_ylabel('log(y)')
ax[2].grid(True)

plt.show()
plt.close()
