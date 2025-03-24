#!/usr/bin/python3.8.10
#used Prof. Joyce's lu decomposition code in my_functions_lib
import numpy as np
import sys
sys.path.insert(0, '/home/noahh/PHYS_4840')
import my_functions_lib as mfl
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

