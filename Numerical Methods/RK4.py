def f(x, y):
    return 2*x*y


x0 = 0
y0 = 1
h = 0.1
xn = 2
x = x0
y = y0
while x < xn:
    k1 = h*f(x, y)
    k2 = h*f(x + h/2, y + k1/2)
    k3 = h*f(x + h/2, y + k2/2)
    k4 = h*f(x + h, y + k3)
    y += (k1 + 2*k2 + 2*k3 + k4)/6
    x += h
print("Approximate solution at x =", xn, "is", round(y, 4))
