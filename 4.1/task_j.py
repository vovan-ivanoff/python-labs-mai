"""задание j: Слияние"""


def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def merge(arr1, arr2):
    result = arr1 + arr2
    return tuple(bubbleSort(list(result)))
