# Program for the linear search algoritm
def search(arr, n, x): 
    for i in range (n): 
        if (arr[i] == x): 
            return i
    return -1
print("This is the program to search for an element in an given array")
arr = [int(x) for x in input("Enter the array elements : ").split()] 
x = int(input("Enter the element to be searched : ")) 
n = len(arr)
result = search(arr, n, x) 
if(result == -1): 
    print(str(x) + " is not present in the given array") 
else: 
    print(str(x) + " is present in the given array at index", result)
