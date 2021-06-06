lower = int(input("Enter the lower limit : "))
upper = int(input("Enter the upper limit : "))
count=0
print("Prime numbers between",lower,"and",upper,"are :")
for num in range(lower,upper + 1):
# prime numbers are greater than 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            count+=1
            print(num,end=" ")
if count==0:
    print("No primes in this range")
else:
    print("\nTotal",count,"primes are there in between this range")