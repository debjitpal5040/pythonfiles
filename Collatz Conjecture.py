'''Program to print the sequence generated from Collatz conjecture'''
print("This is the program to print the sequence generated from Collatz conjecture")
n = int(input("Enter a number : "))
while n > 1:
    print(n, end = " ")
    if n % 2 == 0:
        n //= 2
    else:
        n *= 3 
        n+=1
print(1, end='\n')
print("It eventually reaches to 1")