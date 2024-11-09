def find_disappeared_numbers(nums: list[int]) -> list[int]:
    # time solution
    result = []
    for num in nums:
        num = abs(num)
        nums[num - 1] = abs(nums[num - 1]) * -1
    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i + 1)
    return result

    # space solution
    result = []
    nums_set = set(nums)
    for i in range(1, len(nums) + 1):
        if i not in nums_set:
            result.append(i)

    return result


if __name__ == "__main__":
    assert find_disappeared_numbers(nums=[4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert find_disappeared_numbers(nums=[1, 1]) == [2]
