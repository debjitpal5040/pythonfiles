def f(x):
    return x**2
def left_riemann(a, b, n):
    h = (b-a)/n
    s = 0
    for i in range(n):
        s += f(a+i*h)
    return s*h
print(left_riemann(0, 6, 100))

# monotonically increasing :- underestimation
# monotonically decreasing :- overestimation