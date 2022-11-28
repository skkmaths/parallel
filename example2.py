from numba import njit, prange
import numpy as np
import time

@njit(parallel = True)

def sumuptoN(n):
    sum = 0
    for i in range(n+1):
        sum +=i
    return sum

for i in prange(10):
    print(sumuptoN(i))

