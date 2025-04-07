# combine two sorted lists
def sort(arr1: list, arr2: list) -> list:
    result: list = []
    i: int = 0
    j: int = 0
    while i < len(arr1) and j < len(arr2):
        if arr2[j] < arr1[i]:
            result.append(arr2[j])
            j += 1
        else:
            result.append(arr1[i])
            i += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    return result

if __name__ == "__main__":
    print(sort([1, 3, 5, 10, 21], [1, 4, 9, 12]))