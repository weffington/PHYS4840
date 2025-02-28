#!/usr/bin/python3.10.12
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('../')
import my_functions_lib as mfl
#we want h to be equal to c^1/3, where
#c=10^-16 in python
df=[]
h=[10**((-16)/3),2,1]
x=np.linspace(-2,2,100)
for i in range(0,3):
    approxDf=(mfl.f(x+(0.5*h[i])) - mfl.f(x-(0.5*h[i])))/h[i]
    df.append(approxDf)

fig, ax = plt.subplots(figsize=(8,16))
plt.plot(x,df[0],'.g')
plt.plot(x,df[1],'*r')
plt.plot(x,df[2],'xk')
plt.plot(x,mfl.g(x),'r')
plt.legend(['h=10^-5.33','h=2','h=1','derivative'])
plt.show()
plt.close()