def find_duplicates(nums: list[int]) -> list[int]:
    rs = []
    for num in nums:
        num = abs(num)
        if nums[num - 1] < 0:
            rs.append(num)
        else:
            nums[num - 1] = -nums[num - 1]
    return rs


if __name__ == "__main__":
    assert find_duplicates(nums=[4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]
    assert find_duplicates(nums=[1, 1, 2]) == [1]
