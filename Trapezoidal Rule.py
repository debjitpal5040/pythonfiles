def f(x):
    return x**2


def trapezoidal(a, b):
    h = (b-a)
    s = f(a)+f(b)
    return s*h/2


print(trapezoidal(0, 6))


def trapezoidal_composite(a, b, n=1):
    h = (b-a)/n
    s = f(a)+f(b)
    for i in range(1, n):
        s += 2*f(a+i*h)
    return s*h/2


print(trapezoidal_composite(0, 6, 100))

# error analysis
# -((b-a)**3/(12*n**2))*f''(c)
# where a<c<b