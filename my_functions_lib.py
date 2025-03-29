#!/usr/bin/python3.8.10
import numpy as np
def myFunction(vector):
    a = vector[0]
    b = vector[1]
    c = vector[2]

    return np.linalg.norm(vector)

def y(x):
    y=2*x**3.0
    return y

def f(x):
    y = 1 + 0.5*np.tanh(2*x)
    return y

def g(x):
    df=(1/(np.cosh(2*x)))**2
    return df

def trapezoidal(y_values, x_values, N):
    a = x_values[0]
    b = x_values[-1]
    h = (b-a)/N

    integral = (1/2) * (y_values[0] + y_values[-1]) * h  # First and last terms

    for k in range(1, N):
        xk = a + k * h  # Compute x_k explicitly
        yk = np.interp(xk, x_values, y_values)  # Interpolate y at x_k manually in loop
        integral += yk * h

    return integral

def simpsons(y_values, x_values, N):

    a = x_values[0]
    b = x_values[-1]
    h = (b-a)/N

    integral = y_values[0] + y_values[-1] # First and last y_value terms

    for k in range(1, N, 2):  # Odd indices (weight 4)
        xk = a + k * h
        yk = np.interp(xk, x_values, y_values)
        integral += 4 * yk

    for k in range(2, N, 2):  # Even indices (weight 2)
        xk = a + k * h
        yk = np.interp(xk, x_values, y_values)
        integral += 2 * yk

    return (h / 3) * integral  # Final scaling

def romberg(y_values, x_values, max_order):
    R = np.zeros((max_order, max_order))
    a = x_values[0]
    b = x_values[-1]
    N = 1
    h = (b - a)

    # First trapezoidal estimate
    R[0, 0] = (h / 2) * (y_values[0] + y_values[-1])

    for i in range(1, max_order):
        N = 2**i #Remember: we are recomputing the integral with different N (and therefore h)
        h = (b-a)/N #Look at the github derivation for richardson extrapolation

        sum_new_points = sum(np.interp(a + k * h, x_values, y_values) for k in range(1, N, 2))
        R[i, 0] = 0.5 * R[i - 1, 0] + h * sum_new_points

        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / (4**j - 1)

    return R[max_order - 1, max_order - 1]

def qr_decomposition(A):
    ## Computes the QR decomposition of matrix A using
    ## Gram-Schmidt orthogonalization.
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for j in range(n):
        v = A[:, j]  # Take column j of A
        for i in range(j):  # Subtract projections onto previous Q columns
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)  # Compute norm
        Q[:, j] = v / R[j, j]  # Normalize

    return Q, R

def lu_decomposition(A):
    N = len(A)

    # Initialize L as the N=4 identity matrix 
    L = np.array([[1.0 if i == j else 0.0 for j in range(N)] for i in range(N)])
    # this above is just a more explicit way of doing
    #L = np.identity(N)


    # initalize U as a copy of A
    U = A.copy()


    ## this double loop will transform L
    ## into the lower-diagonal form we need
    for m in range(N):
        for i in range(m+1, N):        
        
            # Compute the multiplier for the current row operation
            L[i, m] = U[i, m] / U[m, m]
        
            # Subtract the appropriate multiple of the pivot row from the current row
            U[i, :] -= L[i, m] * U[m, :]

    return L, U

def euler_method(f, x0, t0, t_end, dt): 
    #define range of t values using step size dt
    t_values=np.arange(t0, t_end+dt,dt)
    #define 0 array for future x values
    x_values=np.zeros(len(t_values))
    #initial condition
    x_values[0]=x0
    #iterate using euler's method to get x values
    for i in range(1, len(t_values)):
        x_values[i]=x_values[i-1] + dt * f(x_values[i-1], t_values[i-1])
    #return approximation for x(t) and corresponding t values
    return t_values, x_values