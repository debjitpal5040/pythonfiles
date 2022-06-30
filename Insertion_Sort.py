# In-place: Yes
# Stable: Yes
# Time Complexity: O(n^2)
# Space Complexity: O(1)
arr = [34, 56, 92, 49, 12, 36]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


print(insertion_sort(arr))
