def binary_search_iterative(arr, n, x):
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

# time complexity of binary search is O(log n)
