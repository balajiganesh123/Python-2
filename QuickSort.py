def partition(arr, left, right):
    i, j = left, right - 1
    pivot = arr[right]
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i

def quickSort(arr, left, right):
    if left < right:
        partitionPos = partition(arr, left, right)
        quickSort(arr, left, partitionPos - 1)
        quickSort(arr, partitionPos + 1, right)

arr = [19, -76, -6, -972, 84, 281, 56]
print(arr)
quickSort(arr, 0, len(arr) - 1)
print(arr)