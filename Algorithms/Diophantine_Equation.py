# Given three numbers a>=0, b>=0, and c, the algorithm should return some x and y such that
# ax+by=c
from math import gcd


def diophantine(a, b, c):
    if a == 0 and b == 0:
        if c == 0:
            return "x : Any integer, y : Any integer"
        else:
            return "No integral solution exists"
    if a == 0:
        if c % b == 0:
            return "x : Any integer, y = " + str(c//b)
        else:
            return "No integral solution exists"
    if b == 0:
        if c % a == 0:
            return "x = " + str(c//a) + ", y : Any integer"
        else:
            return "No integral solution exists"
    if c % gcd(a, b) == 0:
        # divmod operation to compute the quotient and remainder at the same time
        q, r = divmod(a, b)
        if r == 0:
            return [0, c//b]
        else:
            sol = diophantine(b, r, c)
            u = sol[0]
            v = sol[1]
            return [v, u - q*v]
    else:
        return "No integral solution exists for this diophantine equation"


print("Enter the coefficients of the equation ax + by = c")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print(diophantine(a, b, c))
