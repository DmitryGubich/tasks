def max_ascending_sum(nums: list[int]) -> int:
    result = cur = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            cur += nums[i]
        else:
            cur = nums[i]
        result = max(result, cur)
    return result


if __name__ == "__main__":
    assert max_ascending_sum(nums=[10, 20, 30, 5, 10, 50]) == 65
    assert max_ascending_sum(nums=[12, 17, 15, 13, 10, 11, 12]) == 33
