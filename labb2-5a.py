import math

def derivative(f, x, h):
    k =(1.0/(2*h))*(f(x+h)-f(x-h))
    return k

##print derivative(math.sin, math.pi, 0.0001)
##print derivative(math.cos, math.pi, 0.0001)
##print derivative(math.tan, math.pi, 0.0001)

def solve(f, x0, h):
    lastX = x0
    new = 0.0
    while (abs(lastX) - abs(new) > h) or lastX==new:
        new = lastX
        lastX = lastX - f(lastX)/derivative(f, lastX, h)
    return lastX


def function1(x):
    return x**2-1

def function2(x):
    return 2**x-1

def function3(x):
    x-cmath.e**-x
    
print solve(function2, 4, 0.00001)
