"""Python program for modular exponentiation"""
# Iterative Function to calculate (x^y)%p in O(log y)
def power(x, y, p) :
    res = 1
    if (x >= p) :
        x %= p
    if (x == 0) :
        return 0
    while (y > 0) :
        if ((y % 2) == 1) :
            res = (res * x) % p	 # If y is odd, multiply x with result
        y //= 2
        x = (x * x) % p
    return res

x = int(input("Number : ")) 
y = int(input("Power : ")) 
p = int(input("Modulus : "))
print("Remainder is", power(x, y, p))