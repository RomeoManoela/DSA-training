def selection_sort(arr: list) -> list:
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


print(selection_sort([5, 4, 3, 2, 40, 1]))
