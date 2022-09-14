from math import *

def df(f, x, dx=0.00001):
    return (f(x+dx)-f(x))/dx

print('df(sin, pi/4)=', df(sin, pi/4))
