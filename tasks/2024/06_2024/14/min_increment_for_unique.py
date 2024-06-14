def min_increment_for_unique(nums: list[int]) -> int:
    nums.sort()
    tracker, result = 0, 0

    for num in nums:
        tracker = max(tracker, num)
        result += tracker - num
        tracker += 1
    return result


if __name__ == "__main__":
    assert min_increment_for_unique(nums=[1, 2, 2]) == 1
    assert min_increment_for_unique(nums=[3, 2, 1, 2, 1, 7]) == 6
