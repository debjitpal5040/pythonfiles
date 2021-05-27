# program to count total number of divisors 
print("This is the program to count total number of factors of a number")
def countDivisors(n) :
    if n==1:
        return 1
    cnt = 2
    for i in range(2, int(n**0.5) + 1) :
        if (n % i == 0) :
            if (n / i == i) :
                cnt += 1
            else : 
                cnt += 2
    return cnt
n=int(input("Enter the number : "))
print("Number of divisors of",n,"is :",countDivisors(n))