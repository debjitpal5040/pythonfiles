lower = int(input("Enter the lower limit : "))
upper = int(input("Enter the upper limit : "))
Sum=0
for num in range(lower,upper + 1):
# prime numbers are greater than 1
    if num > 1:
        for i in range(2,int(num**0.5)+1):
            if (num % i) == 0:
                break
        else:
            Sum+=num
print("Sum of Prime numbers between",lower,"and",upper,"are :",Sum)