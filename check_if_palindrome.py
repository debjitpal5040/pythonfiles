# Program to check if a number is palindrome or not
print("This is the program to check if a given number is palindrome or not")
Number = input("Please Enter any Number : ")
print(Number,"is a Palindrome" if Number==Number[::-1] else "is not a Palindrome")