# Given three integers a, b, and n,the algorithm should return an integer x such that 
# ax≡b(modn) where 0≤x≤n−1 
from math import gcd
def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y

def divide(a, b, n):
  if b % gcd(a,n)!= 0 :
    return "No integral solution"
  d, t, s = gcdExtended(a,n)
  if t < 0:
    t +=  n
    return t * b % n
  else:
    return t * b % n

print("Enter the coefficients of the equation ax ≡ b(mod n)")
a = int(input("a : "))
b = int(input("b : "))
n = int(input("n : "))
print("x =",divide(a,b,n))