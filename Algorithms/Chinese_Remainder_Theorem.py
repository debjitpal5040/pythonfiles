# returns the solution of the simultaneous linear equation pair x≡a1(mod n1) and x≡a2(mod n2) where gcd(n1,n2)=1


def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y


def divide(a, b, n):
    _, t, _ = gcdExtended(a, n)
    if t < 0:
        t += n
        return t * b % n
    else:
        return t * b % n


def ChineseRemainderTheorem(a1, n1, a2, n2):
    x1 = divide(n2, 1, n1)
    x2 = divide(n1, 1, n2)
    return a1*x1*n2 + a2*x2*n1


print("Enter coefficients of the equations x≡a1(mod n1) and x≡a2(mod n2)")
a1 = int(input("a1 : "))
n1 = int(input("n1 : "))
a2 = int(input("a2 : "))
n2 = int(input("n2 : "))
print("x =", str(ChineseRemainderTheorem(a1, n1, a2, n2)))
