# In-place: No
# Stable: Yes
# Online: No
# Adaptive: No
# Best case is O(n log n) when the array is already sorted.
# Worst case is O(n log n) when the array is reverse sorted.
# Space Complexity: O(n)

arr = [34, 21, 12, 9, 5, 6, 10, 100, 0, 48, -1]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result


print(merge_sort(arr))
