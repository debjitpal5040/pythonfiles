# In-place: Yes
# Stable: No
# Adaptive: Yes
# Online: No

# Best and Average case Time Complexity: O(n log n) [pivot is chosen as median]
# Worst case Time Complexity: O(n^2) [This happens when input array is sorted or reverse sorted and either first or last element is picked as pivot.]
# Space Complexity: O(log n)

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
