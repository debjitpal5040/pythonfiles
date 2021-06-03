# count total number of primes less than or equal to a number
upper = int(input("Enter the upper limit : "))
if upper > 2:
    count=1
    for num in range(3,upper + 1,2):
        # prime numbers are greater than 1
        for i in range(3,num,2):
            if (num % i) == 0:
                break
        else:
            count+=1
    print("Total Number of primes less than or equal to",upper,"is :",count)
elif upper==2:
    print("Total Number of primes less than or equal to 2 is : 1")
else:
    print("Total Number of primes less than or equal to",upper,"is : 0")
"""
Time complexity : O(n^2)
"""