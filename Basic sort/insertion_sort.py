def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        temp: int = arr[i]
        j: int = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            arr[j] = temp
            j = j - 1
        # for j in range(i, 0, -1):
        #     if arr[j] < arr[j - 1]:
        #         arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


print(insertion_sort([5, 4, 3, 2, 40, 1]))
