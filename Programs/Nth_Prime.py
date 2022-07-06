print("This is the program to find the nth prime number")
def nthprime(n):
    start = 2
    count = 0
    while True:
        if all([start % i for i in range(2, int(start**0.5) + 1)]) != 0:
            count += 1
            if count == n:
                return start
        start += 1 
nth = int(input("Enter the value of n : "))
print("The answer is :",nthprime(nth))