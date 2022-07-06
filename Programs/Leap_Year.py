# Program to find whether a year is leap or not
print("This is a program to check if a year is leap or not")
year = int(input("Enter a year : "))
print(str(year)+ " is a leap year" if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)) else str(year)+" isn't a leap year")