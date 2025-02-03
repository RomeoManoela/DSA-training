# concatenate two ordered list and return a new ordered list
def fusion(list1: list, list2: list) -> list:
    new_lst: list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            new_lst.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            new_lst.append(list2[j])
            j += 1
    while i < len(list1):
        new_lst.append(list1[i])
        i += 1
    while j < len(list2):
        new_lst.append(list2[j])
    return new_lst

# find the second max value in a list of float number
def find_second(numbers: list[float]) -> float:
    max_num = max(numbers)
    result: float = 0
    for num in numbers:
        if num > result and num != max_num:
            result = num
    return result

# even before and not even after
def reorder(numbers: list[int]) -> None:
    odds: list[int] = [num for num in numbers if num % 2 == 1]
    even: list[int] = [num for num in numbers if num % 2 == 0]
    numbers[:] = even + odds

# remove elements
def clear_list(lst: list) -> None:
    unique: list = []
    for num in lst:
        if num not in unique:
            unique.append(num)
    lst[:] = unique

def main():
    # print(fusion([1, 2, 9], [4, 5, 6]))
    # print(find_second([1, 2, 9, 8, 0]))
    # print([1, 2, 9, 8, 0].index(2))
    lst: list[int] = [ i for i in range(10) ]
    print(lst)
    reorder(lst)
    print(lst)
    l: list = ['a', 'b', 'c', 'a', 'b', 1, 1, 2, 4]
    clear_list(l)
    print(l)
if __name__ == '__main__':
    main()