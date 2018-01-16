from numba import *

@ jit
def a():
    return (2 ** 1000) / 2016

print(a())