# Program to check if a number is prime or not
print("This is a program to check if a number is prime or not")
N = int(input("Please Enter a Number : "))
# 1 is neither a prime nor a composite number
if N == 1:
    print("1 is neither a prime nor a composite number")
# 2 is the only even prime number
elif N == 2:
    print("2 is a prime number") 
# All odd primes are greater than 2
elif N > 2:
    # check if even
    if N%2==0:
        print(N,"is not a prime number")
        print(str(N)+' = '+str(2)+' × '+str(N//2))
    # check for factors
    else:
        for i in range(3,int(N**0.5)+1,2):
            if (N % i) == 0:
                print(N,"is not a prime number")
                print(str(N)+' = '+str(i)+' × '+str(N//i))
                break
        else:
            print(N,"is a prime number")
# if input number is less than 1, it is not a valid input
else:
    print("Invalid Input")