# In-place: Yes
# Stable: No
# Online: Yes
# Adaptive: No
# Space Complexity: O(1)
# Both Best case and Worst case is O(n^2)
# n(n-1)/2 swaps for Best and Worst Case
# 0 swaps for Best Case and 3(n-1)/2 for Worst Case
arr = [34, 56, 92, 49, 12, 36]


def selection_sort(arr):
    for i in range(len(arr)):
        id = arr.index(min(arr[i:]))
        arr[i], arr[id] = arr[id], arr[i]
    return arr


print(selection_sort(arr))
