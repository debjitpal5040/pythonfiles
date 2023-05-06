# In-place: Yes
# Stable: Yes
# Online: Yes
# Adaptive: Yes
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Best case is O(n) when the array is already sorted.
# Here (n-1) comparisons are made and 0 movements.
# Worst case is O(n^2) when the array is reverse sorted.
# Here (n(n-1))/2 comparisons are made and (n(n-1))/2 movements.
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
