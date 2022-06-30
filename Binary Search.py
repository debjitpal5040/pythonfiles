def binary_search(arr, n, x):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursive(arr, n, x):
    if n == 0:
        return -1
    mid = n // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return binary_search_recursive(arr[mid + 1:], n - mid - 1, x)
    else:
        return binary_search_recursive(arr[:mid], mid, x)


print("This is the program to search for an element in an given array")
arr = [int(x) for x in input("Enter the array elements : ").split()]
x = int(input("Enter the element to be searched : "))
n = len(arr)
result = binary_search(arr, n, x)
if(result == -1):
    print(str(x) + " is not present in the given array")
else:
    print(str(x) + " is present in the given array at index", result)
res = binary_search_recursive(arr, n, x)
if res != -1:
    print("Element found at index", result)
else:
    print("Element not found")
