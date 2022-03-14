'''
In mathematics, the bisection method is a root-finding method that applies to any continuous functions 
for which one knows two values with opposite signs. The method consists of repeatedly bisecting the interval
defined by these values and then selecting the subinterval in which the function changes sign, and 
therefore must contain a root. It is a very simple and robust method, but it is also relatively slow. Because of this, 
it is often used to obtain a rough approximation to a solution which is then used as a starting point for more 
rapidly converging methods. The method is also called the interval halving method, the binary search method, or the dichotomy method.
'''
def f(x):
    from math import exp
    return x*exp(x)-1

def bisection(a, b, iterations):
    if f(a)*f(b) > 0:
        return 'f(a) and f(b) have the same sign, either no root exists or there are even number of roots in this interval'
    else:
        N = 1
        while N <= iterations:
            c = (a+b)/2
            if f(c) == 0:
                return c
            if f(a)*f(c) < 0:
                b = c
            else:
                a = c
            N += 1
        return c

print(bisection(0, 1, 12))