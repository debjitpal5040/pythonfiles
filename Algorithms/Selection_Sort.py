# In-place: Yes
# Stable: No
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Both Best case and Worst case is O(n^2)
# n(n-1)/2 comparisons for Best and Worst Case
# 0 movements for Best Case and 3(n-1)/2 for Worst Case
arr = [34, 56, 92, 49, 12, 36]


def selection_sort(arr):
    for i, _ in enumerate(arr):
        _id = arr.index(min(arr[i:]))
        arr[i], arr[_id] = arr[_id], arr[i]
    return arr


print(selection_sort(arr))
