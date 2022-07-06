def f(x):
    return x**2


def midpoint(a, b):
    h = (b-a)
    s = f((a+b)/2)
    return s*h


print(midpoint(0, 6))


def midpoint_composite(a, b, n=1):
    h = (b-a)/n
    s = 0
    for i in range(1, n+1):
        s += f(a+(2*i-1)*h/2)
    return s*h


print(midpoint_composite(0, 6, 100))

# error analysis
# ((b-a)**3/(24*n**2))*f''(c)
# where a<c<b