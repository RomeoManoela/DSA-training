from pivot import pivot_function
def quick_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums
    pivot = pivot_function(nums)
    left: list[int] = quick_sort(nums[:pivot])
    right: list[int] = quick_sort(nums[pivot + 1:])
    return left + [nums[pivot]] + right

if __name__ == "__main__":
    print(quick_sort([4, 6, 1, 7, 3, 2, 5]))