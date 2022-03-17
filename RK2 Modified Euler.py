def f(x, y):
    return 2*x*y


x0 = 0
y0 = 1
h = 0.01
xn = 2
x = x0
y = y0
while x < xn:
    k1 = h * f(x, y)
    k2 = h * f(x + h , y + k1)
    y += (k1 + k2) / 2
    x += h

print("Approximate solution at x =", xn, "is", round(y, 4))
