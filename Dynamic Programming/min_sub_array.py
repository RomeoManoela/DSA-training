def min_sub_array(nums) -> int:
    if len(nums) == 0:
        return 0
    min_sum = float("inf")
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sub_array = nums[i:j]
            min_sum = min(min_sum, sum(sub_array))
    return min_sum


# with dp
def min_sub_array2(nums):
    if len(nums) == 0:
        return 0
    min_sum = current_min = nums[0]
    for i in range(1, len(nums)):
        current_min = min(current_min, nums[i] + current_min)
        min_sum = max(min_sum, current_min)
    return min_sum


if __name__ == "__main__":
    print(min_sub_array([1, 2, 3, 4, 5]))
    print(min_sub_array2([1, 2, 3, 4, 5]))
