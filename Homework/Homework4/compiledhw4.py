#!/usr/bin/python3.8.10
import numpy as np
from numpy.linalg import eigvals
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '/home/noahh/PHYS_4840')
import my_functions_lib as mfl

#Problem 2
#a)
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

#e)
def gamma(a):
    z=np.linspace(0,1,1000)
    c=a-1
    x=(c*z)/(1-z)
    y=np.where(z != 1, c*(np.exp((c*np.log(x)) - x)/((1-z)**2)), 0)
    gamma=mfl.romberg(y,z,10)
    if a==int(a):
        return round(gamma)
    else:
        return gamma
print(f"gamma(3/2): {gamma(3/2)}")

#f)
print(f"\ngamma(3): {gamma(3)}")
print(f"\ngamma(6): {gamma(6)}")
print(f"\ngamma(10): {gamma(10)}")

#Problem 3
A=np.array([[1,0,0,0],[0,1,1,-1],[0,2,4,0],[0,2,-1,2]],float)
v=np.array([0,294.3,392.4,196.2],float)

#2
LU=mfl.lu_decomposition(A)
QR=mfl.qr_decomposition(A)
L=LU[0]
U=LU[1]
print(f"Lower diagonal matrix (L):\n{L}\nUpper diagonal matrix (U):\n{U}")
Q=QR[0]
R=QR[1]
print(f"Q matrix:\n{Q}\nR Matrix:\n{R}")

#3
Q_T=np.transpose(Q)
print(f"Q transpose:\n{Q_T}")
print(f"Q times Q transpose:\n{np.matrix.round(Q@Q_T)})")
print(f"Q times R:\n{np.matrix.round(Q@R)}")

#Problem 5
#used np.linalg.eigvals
#We can compute the eigenvalues for each matrix as they are all square

#Matrix 1
A_1=np.array([[4,1],
              [2,3]],float)
print(f"The eigenvalues for Matrix 1 are {eigvals(A_1)}.")

#Matrix 2
A_2=np.array([[1,2,3],
              [0,1,4],
              [0,0,1]],float)
print(f"\nThe eigenvalues for Matrix 2 are {eigvals(A_2)}.")

#Matrix 3
A_3=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]],float)
print(f"\nThe eigenvalues for Matrix 3 are {np.matrix.round(eigvals(A_3),5)}.")

#Matrix 4
A_4=A_3=np.array([[1,2,3],
              [4,5,6],
              [7,8,10]],float)
print(f"\nThe eigenvalues for Matrix 3 are {np.matrix.round(eigvals(A_4),5)}.")