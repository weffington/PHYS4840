#!/usr/bin/python3.10.12
import numpy as np
def myFunction(vector):
    a = vector[0]
    b = vector[1]
    c = vector[2]

    return np.linalg.norm(vector)

def y(x):
    y=2*x**3.0
    return y