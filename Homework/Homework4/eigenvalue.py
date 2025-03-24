#!/usr/bin/python3.8.10
#used np.linalg.eigvals
import numpy as np
from numpy.linalg import eigvals
import sys
sys.path.insert(0, '/home/noahh/PHYS_4840')
import my_functions_lib as mfl
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
