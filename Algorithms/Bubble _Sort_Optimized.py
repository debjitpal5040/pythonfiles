array = [2, 7, 4, 5]


def optimizedBubbleSort(arr):
    n = len(arr)
    for i in range(n):
        flag = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                flag = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not flag:
            break
    return arr


print(optimizedBubbleSort(array))
