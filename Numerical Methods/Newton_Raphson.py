'''
In numerical analysis, Newton's method, also known as the Newton-Raphson method, named after Isaac Newton 
and Joseph Raphson, is a root-finding algorithm which produces successively better approximations to the roots
(or zeroes) of a real-valued function. The most basic version starts with a single-variable function f defined for 
a real variable x, the function's derivative f', and an initial guess x0 for a root of f. If the function 
satisfies sufficient assumptions and the initial guess is close, then is a better approximation of the root than x0. 
Geometrically, (x1, 0) is the intersection of the x-axis and the tangent of the graph of f at (x0, f(x0)): that is, 
the improved guess is the unique root of the linear approximation at the initial point. The process is repeated as
until a sufficiently precise value is reached. This algorithm is first in the class of Householder's methods,
succeeded by Halley's method. The method can also be extended to complex functions and to systems of equations. 
'''
def f(x):
    from math import exp
    return x*exp(x)-1


def f_prime(x):
    from math import exp
    return exp(x) + x*exp(x)


def newton_raphson(x, iterations):
    N = 1
    while N <= iterations:
        x = x - (f(x)/f_prime(x))
        N += 1
    return x

print(newton_raphson(1, 3))

# failure analysis
'''
https://en.wikipedia.org/wiki/Newton%27s_method#Failure_analysis

Bad starting points
Iteration point is stationary
Starting point enters a cycle
Derivative does not exist at root
Discontinuous derivative
'''