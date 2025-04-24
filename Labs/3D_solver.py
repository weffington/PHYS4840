#!/usr/bin/python3.8
#####################################
#
# Class 23: PDEs I: 3D Laplace Solver
# Author: Adapted by M Joyce from Mark Newman
# Edits made by Noah Hampton
#####################################
import numpy as np
import matplotlib.pyplot as plt

# Constants
N = 30             # Grid size (cube of size N x N x N)
h = 1               # Grid spacing
V = 1.0             # Voltage on the top face (z = 0)
target = 1e-6       # Convergence criterion

# Initialize the potential arrays
phi = np.zeros((N+1, N+1, N+1), dtype=float)
phinew = np.empty_like(phi)

# Apply boundary condition: top face (z = 0) at V, others at 0
phi[:,:,0] = V

# Iterative solution using Gauss-Seidel-like update
delta = 1.0
iteration = 0
while delta > target:
    iteration += 1
    for i in range(1, N):
        for j in range(1, N):
            for k in range(1, N):
                phinew[i,j,k] = (phi[i+h,j,k] + phi[i-h,j,k] +
                                 phi[i,j+h,k] + phi[i,j-h,k] +
                                 phi[i,j,k+h] + phi[i,j,k-h]) / 6.0

    # Preserve boundary conditions
    phinew[:,:,0] = V
    phinew[:,:,N] = 0
    phinew[:,0,:] = 0
    phinew[:,N,:] = 0
    phinew[0,:,:] = 0
    phinew[N,:,:] = 0

    delta = np.max(np.abs(phi - phinew))
    phi, phinew = phinew, phi

    if iteration % 10 == 0:
        print(f"Iteration {iteration}, max delta = {delta:.2e}")

# Visualization: middle slice in z-direction
mid_z = 0
plt.figure(figsize=(6,5))
plt.imshow(phi[:,:,mid_z], origin='lower', cmap='inferno')
plt.colorbar(label='Potential $\Phi$')
plt.title(f"Midplane slice at z = {mid_z}")
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.show()

'''
a)
We want to add 2 extra difference terms corresponding to the +z and -z directions
to extend our 2d approximation to 3d.

b)
A small grid size gives us a reasonable volume for our cube to iterate over, 
which in turn allows us to calculate and plot our phi approximation much faster. 
This can be seen by setting N=100 and observing how much slower our 
approximation converges.

c)
A higher convergence criterion gives a faster computing time, but a less uniform plot.
A lower convergence criterion gives a more uniform and accurate plot,
but takes longer to compute

d)
In the 2d case, the boundary conditions are preserved on the edges of the square, with
the top edge equal to V. In the 3d case, the boundary conditions are preserved
on the edges of the cube, so the boundary conditions correspond to an certain NxN
matrix of values.

'''