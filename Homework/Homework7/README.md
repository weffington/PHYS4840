# Problem 2
The MESA papers use Runge-Kutta in their module `num`. This module is used to numerically approximate the solutions to each equation in the equations of steller structure.
# Problem 3
This problem solves the equation of mass conservation in the equations of stellar structure. The boundary conditions are $r=0$, $r_{end}=10$, and $m=0$ and they are enforced by iterating over $r$ with starting and ending values equal to $0$ and $10$ respectively. 

When plotting the data outputted by the code, we get a plot where $r$ should be on
the x-axis and $m$ should be on the y-axis, where $r$ is the radius of the star and $m$ is its mass.

# Problem 4
An elliptic partial differential equation has solutions defined throughout their entire domain. An example of an elliptic partial differential equation is Laplace's equation: $\nabla^2 \phi = 0$.

A parabolic partial differential equation has solutions that smooth out as time evolves. An example of a parabolic differential equation is the heat equation: $\frac{\partial \phi}{\partial t} = \nabla^2 \phi$.

A hyperbolic partial differential equation has solutions that retain discontinuities of functions of the initial conditions. An example of a hyperbolic partial differential equation is the wave equation:
$\frac{\partial^2 \phi}{\partial t^2} = \frac{1}{v^2} \nabla^2 \phi$