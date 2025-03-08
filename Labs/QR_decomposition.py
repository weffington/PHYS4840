#!/usr/bin/python3.8
#####################################
#
# Class 14: Matrices and Linear algebra 
# Author: M Joyce
#
#####################################
import numpy as np
import sys
sys.path.append('../')
import my_functions_lib as mfl

'''
by importing and using the QR decomposition 
algorithm in my_functions_lib.py:
1) Find Q and R
2) Confirm that Q is orthogonal
3) Confirm that R is upper triangular
4) Confirm that the matrix A introduced in eigenvalues.py
can indeed be reconstructed by the dot product 
of matrices Q and R
'''
A = np.array([ [2, -1, 3,],\
			   [-1, 4, 5], 
			   [3,  5, 6] ],float)
QR=mfl.qr_decomposition(A)
Q=QR[0]
R=QR[1]
print(f"R matrix:\n{R}")
print(f"\nQ matrix:\n{Q}")
Q_t=np.transpose(Q)
print(f"\nQ transpose:\n{Q_t}")
ortho_prod=np.matrix.round(Q@Q_t,5)
ortho_prod=ortho_prod.astype(int)
print(f"\nProduct of Q and Q transpose:\n{ortho_prod}")
A1=Q@R
print(f"\nProduct of Q and R:\n{A1}")