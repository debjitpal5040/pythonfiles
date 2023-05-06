"""Python program to demonstrate Basic Euclidean Algorithm"""
# returns gcd(a,b)


def gcd(a, b):
    if a < 0:
        a = abs(a)
    if b < 0:
        b = abs(b)
    if a == 0:
        return b
    while b > 0:
        a = b
        b = a % b
    return a


a = int(input("First number : "))
b = int(input("Second number : "))
print("gcd(", a, ",", b, ") = ", gcd(a, b))
