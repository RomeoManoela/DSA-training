def pivot_function(lst: list[int]) -> int:
    if len(lst) == 1:
        return 0
    pivot: int = 0
    swap: int = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[pivot]:
            swap += 1
            if swap != i:
                lst[swap], lst[i] = lst[i], lst[swap]
    lst[swap], lst[pivot] = lst[pivot], lst[swap]
    print(lst)
    return swap


if __name__ == "__main__":
    print(pivot_function([4, 6, 1, 7, 3, 2, 5]))
