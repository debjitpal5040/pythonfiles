# In-place: Yes
# Stable: Yes
# Online: No
# Adaptive: Yes
# Worst and Average case Time Complexity: O(n^2) and O(n^2) swaps
# Best case Time Complexity: O(n) and O(1) swaps
# Space Complexity: O(1)
array = [34, 56, 92, 49, 12, 36]


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubble_sort(array))
