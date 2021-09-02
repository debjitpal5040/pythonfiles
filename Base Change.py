""" Python program to convert a number from base A to base B"""

# Function to return ASCII value of a character
def val(c):
	if (c >= '0' and c <= '9'):
		return ord(c) - 48  # For "0","1","2",...,"9"
	else:
		return ord(c) - 55  # For "A","B","C",... etc characters

# Function to convert a number from given base to decimal number
def toDeci(strr, base):
	lenn = len(strr)
	num = 0
	for i in range(lenn):
		if (val(strr[i]) >= base):
			print("Invalid Number") # A digit in input number must be less than the base
			return -1
		num += val(strr[i]) * pow(base,lenn-1-i)
	return num

# Function to return equivalent character of a given value
def reVal(num):
	if (num >= 0 and num <= 9):
		return chr(num + 48)
	else:
		return chr(num + 55)

# Function to convert a given decimal number to a given base
def fromDeci(base, inputNum):
	res = ""
	while (inputNum > 0):
		res += reVal(inputNum % base)
		inputNum //= base
	res = res[::-1] # Reverse the result
	return res

# Function to convert a given number from a base to another base
def convertBase(s, a, b):
	num = toDeci(s, a)  # Convert the number from base A to decimal
	ans = fromDeci(b, num)	# Convert the number from decimal to base B
	print(ans)

s = input("Number to convert : ")
a = int(input("Current base : "))
b = int(input("Expected base : "))

convertBase(s, a, b)