import merge1
def merge_sort(arr: list) -> list:
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge1.sort(left, right)

if __name__ == "__main__":
    print(merge_sort([1, 3, 4, 2]))