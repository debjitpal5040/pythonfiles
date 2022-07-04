'''
In mathematics, the regula falsi, method of false position, or false position method 
is a very old method for solving an equation with one unknown; this method, in modified form,
is still in use. In simple terms, the method is the trial and error technique of using test ("false") values for the variable and then adjusting the test value according to the outcome. This is sometimes also referred to as "guess and check". Versions of the method predate the advent of algebra and the use of equations. 
'''
def f(x):
    from math import log10
    return 2*x - log10(x) - 7

def regula_falsi(a,b,iterations):
    if f(a)*f(b) > 0:
        return 'f(a) and f(b) have the same sign, either no root exists or there are even number of roots in this interval'
    else:
        N = 1
        while N <= iterations:
            x = (a*f(b)-b*f(a))/(f(b)-f(a))
            if f(x) == 0:
                return x
            if f(a)*f(x) < 0:
                b = x
            else:
                a = x
            N += 1
        return x 

print(regula_falsi(3,4,2))