from merge1 import merge

def merge_2(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums
    middle = len(nums) // 2
    left = merge_2(nums[:middle])
    right = merge_2(nums[middle:])
    return merge(left, right)

if __name__ == "__main__":
    print(merge_2([1, 3, 5, 1, 4, 2, 9, 0, 11]))