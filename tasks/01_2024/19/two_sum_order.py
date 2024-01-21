def two_sum_order(nums: list[int], target: int) -> bool:
    left = 0
    right = len(nums) - 1

    while left < right:
        cur = nums[left] + nums[right]
        if cur == target:
            return True
        if cur > target:
            right -= 1
        else:
            left += 1


if __name__ == "__main__":
    assert two_sum_order(nums=[1, 2, 4, 6, 8, 9, 14, 15], target=13) is True
    assert two_sum_order(nums=[-1000, -1, 0, 1], target=1) is True
