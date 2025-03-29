import numpy as np
import matplotlib.pyplot as plt
def f(x,t):
    return -x**3 + np.sin(t)
t0 = 0
t_end=10
N=[10,20,50,100]
dt=np.divide((t_end-t0),N)
tpoints=[]
for i in range(len(N)):
    trange=np.arange(t0,t_end+dt[i],dt[i])
    tpoints.append(trange)
xpoints=[]
enumerate
for i, tvals in enumerate(tpoints):
    x=0
    xvals=[]
    for t in tvals:
        xvals.append(x)
        k1 = dt[i]*f(x,t)
        k2 = dt[i]*f(x+0.5*k1, t+0.5*dt[i])
        x += k2
    xpoints.append(xvals)

for i in range(len(tpoints)):
    plt.plot(tpoints[i],xpoints[i])
plt.xlabel("$t$")
plt.ylabel("$x$")
plt.legend(["$N=10$","$N=20$", "$N=50$", "$N=100$"])
plt.show()
plt.close()