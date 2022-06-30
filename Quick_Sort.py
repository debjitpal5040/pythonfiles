# Time Complexity: O(n log n)
# Space Complexity: O(log n)
# Stable: No
# In-place: Yes
import random
arr = [34, 21, 12, 9, 5, 6, 10, 100, 0, 48, -1]


def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr.pop(random.randint(0, n-1))
    left = [x for x in arr if x <= pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort(arr))
