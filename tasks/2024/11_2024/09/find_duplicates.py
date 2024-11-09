def find_duplicates(nums: list[int]) -> list[int]:
    result = []
    for num in nums:
        num = abs(num)
        if nums[num - 1] < 0:
            result.append(num)
        else:
            nums[num - 1] *= -1
    return result


if __name__ == "__main__":
    assert find_duplicates(nums=[4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]
    assert find_duplicates(nums=[1, 1, 2]) == [1]
