# In-place: Yes
# Stable: No
# Time Complexity: O(n^2)
# Space Complexity: O(1)
arr = [34, 56, 92, 49, 12, 36]


def selection_sort(arr):
    for i in range(len(arr)):
        id = arr.index(min(arr[i:]))
        arr[i], arr[id] = arr[id], arr[i]
    return arr


print(selection_sort(arr))
