# Program for the linear search algoritm
def linear_search_iterative(arr, n, x):
    for i in range(n):
        if (arr[i] == x):
            return i
    return -1


def linear_search_recursive(arr, n, x):
    if n == 0:
        return -1
    elif arr[n-1] == x:
        return n-1
    else:
        return linear_search_recursive(arr, n-1, x)

# Time complexity of linear search is O(n)
