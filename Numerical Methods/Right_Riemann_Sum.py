def f(x):
    return x**2
def right_riemann(a, b, n):
    h = (b-a)/n
    s = 0
    for i in range(1,n+1):
        s += f(a+i*h)
    return s*h
print(right_riemann(0, 6, 100))

# monotonically increasing :- overestimation
# monotonically decreasing :- underestimation