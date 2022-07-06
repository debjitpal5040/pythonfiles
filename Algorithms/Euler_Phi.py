# Program for Euler totient function
print("This is the program for Euler totient function")
def phi(n): 
    result = n 
    p = 2  
    while(p * p <= n):  
        if (n % p == 0):  
            while (n % p == 0): 
                n = n // p 
            result -= result // p
        p += 1  
    if (n > 1): 
        result -= result // n
    return result
n=int(input("Input the value of n : "))
print("phi("+str(n)+")","=",phi(n))