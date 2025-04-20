def merge(list1: list[int], list2: list[int]) -> list[int]:
    i = j = 0
    res: list[int] = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            res.append(list2[j])
            j += 1
        else:
            res.append(list1[i])
            res.append(list2[j])
            i += 1
            j += 1

    while i < len(list1):
        res.append(list1[i])
        i += 1
    while j < len(list2):
        res.append(list2[j])
        j += 1
    return res

if __name__ == "__main__":
    print(merge([3, 7, 9, 12], [2, 5, 7, 10]))