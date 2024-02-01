def divide_array(nums: list[int], k: int) -> list[list[int]]:
    size = len(nums)
    result = []
    nums.sort()

    for i in range(0, size, 3):
        if nums[i + 2] - nums[i] <= k:
            result.append([nums[i], nums[i + 1], nums[i + 2]])
        else:
            return []
    return result


if __name__ == "__main__":
    assert divide_array(nums=[1, 3, 3, 2, 7, 3], k=3) == []
    assert divide_array(nums=[1, 3, 4, 8, 7, 9, 3, 5, 1], k=2) == [
        [1, 1, 3],
        [3, 4, 5],
        [7, 8, 9],
    ]
