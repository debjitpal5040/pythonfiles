arr = [10, 8, 20, 4, 7, 11, 15, 3, 1, 19, 23, 14, 6]


def bucket_sort(arr):
    max_num = max(arr)
    min_num = min(arr)
    bucket_range = (max_num - min_num) // len(arr) + 1
    buckets = [[] for _ in range(len(arr))]
    for value in arr:
        buckets[(value - min_num) // bucket_range].append(value)
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    return sorted_arr


print(bucket_sort(arr))