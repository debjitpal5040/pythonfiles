def f(x):
    return x**2


def simpson1_3(a, b):
    h = (b-a)/2
    s = f(a)+f(b)+4*f((a+b)/2)
    return s*h/3


print(simpson1_3(0, 6))


def simpson1_3_composite(a, b, n=2):
    h = (b-a)/n
    s = f(a)+f(b)
    for i in range(1, n):
        if i % 2 == 0:
            s += 2*f(a+i*h)
        else:
            s += 4*f(a+i*h)
    return s*h/3


print(simpson1_3_composite(0, 6, 100))

# error analysis
# -(1/90)*((b-a)/2)**5*f''''(c)
# where a<c<b