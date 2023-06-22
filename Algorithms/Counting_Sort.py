arr = [2, 9, 7, 4, 1, 2, 8, 4]


def counting_sort(arr):
    max_num = max(arr)
    min_num = min(arr)
    counting_arr_length = max_num - min_num + 1
    counting_arr = [0] * counting_arr_length
    for num in arr:
        counting_arr[num - min_num] += 1
    sorted_arr = []
    for i in range(counting_arr_length):
        if counting_arr[i] > 0:
            sorted_arr.extend([i + min_num] * counting_arr[i])
    return sorted_arr


print(counting_sort(arr))
