# In-place: Yes
# Stable: Yes
# Time Complexity: O(n^2)
# Space Complexity: O(1)
arr = [34, 56, 92, 49, 12, 36]


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubble_sort(arr))
