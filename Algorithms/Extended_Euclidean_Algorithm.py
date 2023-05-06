"""Python program to demonstrate Extended Euclidean Algorithm"""
# returns (x, y, gcd(a,b)) : ax + by = gcd(a,b), x and y are coefficients of Bézout's identity,


def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y


print("Enter the coefficients of the equation ax + by = gcd(a,b)")
a = int(input("a : "))
b = int(input("b : "))
g, x, y = gcdExtended(a, b)
print("x = " + str(x) + ", y = " + str(y) + ", gcd(a,b) = " + str(g))
