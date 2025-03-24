#!/usr/bin/python3.8.10
#a)
import numpy as np
import matplotlib.pyplot as plt
def integrand(x,a):
    integrand=x**(a-1)*np.exp(-x)
    return integrand
x=np.linspace(0,5,1000)
y=integrand(x,3)
for n in range(2,5):
    plt.plot(x,integrand(x,n))
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(['$a=2$','$a=3$','$a=4$'],loc=2)
plt.savefig('Problem2a.png')
plt.show()
plt.close()