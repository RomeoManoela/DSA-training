import math

def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            arr[j] = temp
            j -= 1



    return arr

if __name__ == "__main__":
    print(insertion_sort([57, 8, 74, 0, -5, math.sqrt(8), 4, 3, 2, 1]))