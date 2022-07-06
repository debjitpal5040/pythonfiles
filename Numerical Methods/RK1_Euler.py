def f(x, y):
    return 2*x*y


x0 = 0
y0 = 1
h = 0.01
xn = 2
x = x0
y = y0
while x < xn:
    y += h * f(x, y)
    x += h

print("Approximate solution at x =", xn, "is", round(y, 4))
