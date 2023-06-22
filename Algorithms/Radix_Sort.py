arr = [181, 289, 390, 121, 145, 736, 514, 212]


def radix_sort(arr):
    max_num = max(arr)
    max_num_digits = len(str(max_num))
    sorted_arr = []
    for i in range(max_num_digits):
        buckets = [[] for _ in range(10)]
        for num in arr:
            digit = (num // (10 ** i)) % 10
            buckets[digit].append(num)
        for bucket in buckets:
            sorted_arr.extend(bucket)
    return sorted_arr


print(radix_sort(arr))
