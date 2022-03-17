def f(x, y):
    return 2*x*y


def predict(x, y, h):
    yp = y + h * f(x, y)
    return yp


def correct(x, y, h):
    yc = y + (h/2) * (f(x, y) + f(x+h, predict(x, y, h)))
    return yc


x0 = 0
y0 = 1
xn = 2
h = 0.01
x = x0
y = y0
while (x < xn):
    y = correct(x, y, h)
    x += h
print("The final value of y at x =", xn, "is :", round(y, 4))
