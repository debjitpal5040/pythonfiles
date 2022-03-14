def f(x):
    return x**2


def simpson3_8(a, b):
    h = (b-a)/3
    s = f(a)+f(b)+3*f((2*a+b)/3)+3*f((a+2*b)/3)
    return s*h*3/8


print(simpson3_8(0, 6))


def simpson3_8_composite(a, b, n=3):
    h = (b-a)/n
    s = f(a)+f(b)
    for i in range(1, n):
        if i % 3 == 0:
            s += 2*f(a+i*h)
        else:
            s += 3*f(a+i*h)
    return s*h*3/8


print(simpson3_8_composite(0, 6, 100))

# error analysis
# -(1/6480)*(b-a)**5*f''''(c)
# where a<c<b