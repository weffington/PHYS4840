#!/usr/bin/env python3.10.12
import numpy as np
import matplotlib.pyplot as plt
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





    