def bubbleSort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [19, -76, -6, -972, 84, 281, 56]
print(arr)
bubbleSort(arr)
print(arr)