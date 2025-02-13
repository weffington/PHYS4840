#!/usr/bin/python3.10.12
import numpy as np
import matplotlib.pyplot as plt
#a)
filename='sunspots.txt'
matrix = np.loadtxt('sunspots.txt',float)
length=len(matrix)
x=[]
y=[]
for i in range(0,len(matrix)):
    y.append(matrix[i,1])
    x.append(matrix[i,0])
plt.plot(x,y,'k-')
plt.title('Number of Observed Sunspots Since January 1749')
plt.xlabel('Number of Months Since January 1749')
plt.ylabel('Number of Sunspots')
plt.show()
plt.close()

#b)
plt.plot(x[:1000],y[:1000],'k-')
plt.title('Number of Observed Sunspots Since January 1749')
plt.xlabel('Number of Months Since January 1749')
plt.xlabel('Number of Months Since January 1749')
plt.ylabel('Number of Sunspots')
plt.show()
plt.close()

#c)
Y=[0,0,0,0]
for i in range(5, len(y)-4):
    sumy=[]
    for j in range(i-5,i+5):
        sumy.append(y[j])
    avg=(1/11)*sum(sumy)
    Y.append(avg)
plt.plot(x[:1000],y[:1000],'k-')
plt.plot(x[5:1000],Y[5:1000],'r-')
plt.title('Number of Observed Sunspots Since January 1749')
plt.xlabel('Number of Months Since January 1749')
plt.xlabel('Number of Months Since January 1749')
plt.ylabel('Number of Sunspots')
plt.legend(['Number of Sunspots','Running Average'])
plt.show()
plt.close()




        

    




